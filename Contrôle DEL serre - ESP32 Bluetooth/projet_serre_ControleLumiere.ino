#include <NTPClient.h>
#include <WiFi.h> // for WiFi shield
//#include <WiFi101.h> // for WiFi 101 shield or MKR1000
#include <WiFiUdp.h>
#include <BluetoothSerial.h>

#define etat_out 14

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

const char *ssid     = "cm-public";
const char *password = "sansfil3800";
char value;
String time_utc,time_bt;
int  time_mtl_heure, 
     time_mtl_minute,
     time_mtl_heure_START = 22, 
     time_mtl_minute_START = 00,
     time_mtl_seconde_START = 00,
     time_mtl_heure_FIN = 01,
     time_mtl_minute_FIN = 00;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP);
BluetoothSerial SerialBT;

void setup(){
  Serial.begin(38400);  // vitesse du port serie et du port BT mis a 38400 baud rate
  SerialBT.begin("TGE - minuterie DEL serre"); //Bluetooth device name
  pinMode(etat_out, OUTPUT); // pin de controle de la lumiere
  WiFi.begin(ssid, password);
  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  timeClient.begin();
}

void loop() {
  timeClient.update();
  time_utc = timeClient.getFormattedTime(); // lecture de l'heure selon le protocol NTP
  /*
   * conversion de l'heure UTC en heure UTC-5:00 (Montréal)
   */
  //                          -- 1er octet du string        -- 2eme octet du string
  time_mtl_heure = ((time_utc.charAt(0)-0x30)*10)+(time_utc.charAt(1)-0x30);
  time_mtl_heure = time_mtl_heure-5;
  //                          -- 4eme octet du string        -- 5eme octet du string
  time_mtl_minute = ((time_utc.charAt(3)-0x30)*10)+(time_utc.charAt(4)-0x30);

  /*
   * si l'application BT n'a pas envoyer de nouvelle trame :
   *      - on vérifie qu'on est a l'intérieur de la plage définie lors de la dernières
   *      - si c'est le cas, on allume la lumière
   *      - sinon on la laisse éteinte
   */
  while (!SerialBT.available())
  {
    if((time_mtl_heure >= time_mtl_heure_START) and (time_mtl_heure < time_mtl_heure_FIN))
    {
      //Serial.print("\n\r ON");    // a mettre dans le code pour soucis de dépannage
      digitalWrite(etat_out,HIGH);
    }
    else if((time_mtl_heure >= time_mtl_heure_START) and (time_mtl_minute >= time_mtl_minute_START) and (time_mtl_heure <= time_mtl_heure_FIN) and (time_mtl_minute < time_mtl_minute_FIN))
    {
      //Serial.print("\n\r ON");    // a mettre dans le code pour soucis de dépannage
      digitalWrite(etat_out,HIGH);
    }
    else
    {
      //Serial.print("\n\r OFF");    // a mettre dans le code pour soucis de dépannage
      digitalWrite(etat_out,LOW);
    }
    delay(1000);
  }
  while (SerialBT.available()) {
    value = SerialBT.read();
    time_bt += value;  
  }
  Serial.print(time_bt); 
  /*
   * conversion des données recu par l'application BT de string a int
   */
  //                          -- 1er octet du string        -- 2eme octet du string
  time_mtl_heure_START = (((time_bt.charAt(0/* tres important */)-0x30)*10) + (time_bt.charAt(1)-0x30));
  //                          -- 4eme octet du string       -- 5eme octet du string
  time_mtl_minute_START = (((time_bt.charAt(3/* de verifier*/)-0x30)*10) + (time_bt.charAt(4)-0x30));
  //                          -- 8eme octet du string       -- 9eme octet du string
  time_mtl_heure_FIN = (((time_bt.charAt(7/* les commentaires*/)-0x30)*10) + (time_bt.charAt(8)-0x30));
  //                          -- 11eme octet du string      -- 12eme octet du string
  time_mtl_minute_FIN = (((time_bt.charAt(10)-0x30)*10) + (time_bt.charAt(11)-0x30));
  
  time_bt = ""; // reset du string venant de l'application BT
}


/*
 * Basé sur l'exemple wifi client de l'IDE arduino
 * Modifié par Cédric Vincent, Carlos Mesa A-2019
 *
  Possible changment si nécessaire: Changer le access point en serveur
 *  This sketch sends data via HTTP GET requests to data.sparkfun.com service.
 *
 *  You need to get streamId and privateKey at data.sparkfun.com and paste them
 *  below. Or just customize this script to talk to other HTTP servers.
 *
 */

#include <WiFi.h>

/* L'addresse et le code du point d'accès cible */
const char* ssid     = "HelloJonhny";
const char* password = "TGETSOETUDES";
/*l'addresse ip de l'hôte*/
const char* host = "192.168.4.1";
const char* streamId   = "...................."; // utilisation seulement si l'on utilise les services IOT
const char* privateKey = "....................";
long int sensorPin = 34;    // Pin de l'ADC du capteur
int ledPin = 13;      // select the pin for the LED
long int sensorValue = 0;  // variable to store the value coming from the sensor
void myHandler(int numBytes);
void setup()
{
    Serial.begin(115200);
    delay(10);

    // We start by connecting to a WiFi network
    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

int value = 0;

void loop()
{
    delay(5000);
    ++value;
    sensorValue = analogRead(sensorPin);  // lecture de la valeur du capteur d'humidité
    Serial.print("ADC =");
    Serial.print(sensorValue);
    Serial.print("connecting to ");
    Serial.println(host);

    // Use WiFiClient class to create TCP connections
    WiFiClient client;
    const int httpPort = 80;
    if (!client.connect(host, httpPort)) {
        Serial.println("connection failed");
        return;
    }

    // We now create a URI for the request
    String url = "192.168.4.1 /H";
    url += streamId;
    url += "?private_key=";
    url += privateKey;
    url += "&value=";
    url += value;

    Serial.print("Requesting URL: ");
    Serial.println(url);

    // This will send the request to the server
    if (sensorValue > 2020) // si le capteur d'humidité donne une valeur adc > 50% de sa plage: Humidité en dessous de 50%
    {
    client.print(String("GET /TGETSOETUDESOUVRE") + url + " HTTP/1.1\r\n" + // requête d'ouverture de la valve
                 "Host: " + host + "\r\n" +
                 "Connection: close\r\n\r\n");
    unsigned long timeout = millis();
    while (client.available() == 0) {
        if (millis() - timeout > 5000) {
            Serial.println(">>> Client Timeout !");
            client.stop();
            return;
        }
    }
    }
    else  // sinon: requête de fermeture de la valve
    {
    client.print(String("GET /TGETSOETUDESFerme") + url + " HTTP/1.1\r\n" +
                 "Host: " + host + "\r\n" +
                 "Connection: close\r\n\r\n");
    unsigned long timeout = millis();
    while (client.available() == 0) {
        if (millis() - timeout > 5000) {
            Serial.println(">>> Client Timeout !");
            client.stop();
            return;
        }
    }
    }
    // Read all the lines of the reply from server and print them to Serial
    while(client.available()) {
        String line = client.readStringUntil('\r');
        Serial.print(line);
    }

    Serial.println();
    Serial.println("closing connection");
}

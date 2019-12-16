/*
  WiFiAccessPoint.ino creates a WiFi access point and provides a web server on it.
  Basé sur l'exemple wifi access point de l'IDE arduino
  Modifié par Cédric Vincent, Carlos Mesa A-2019

  Possible changment si nécessaire: Changer le access point en serveur
  Steps:
  1. Connect to the access point "yourAp"
  2. Point your web browser to http://192.168.4.1/H to turn the LED on or http://192.168.4.1/L to turn it off
     OR
     Run raw TCP "GET /H" and "GET /L" on PuTTY terminal with 192.168.4.1 as IP address and 80 as port

  Created for arduino-esp32 on 04 July, 2018
  by Elochukwu Ifediora (fedy0)
*/

#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

#define LED_BUILTIN 13   // Set the GPIO pin where you connected your test LED or comment this line out if your dev board has a built-in LED
#define LED_PRIME 32  // Controleur de Valve
// Addresse du point d'accès créé pour le service //
const char *ssid = "HelloJonhny";
const char *password = "TGETSOETUDES";

WiFiServer server(80);


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_PRIME, OUTPUT);

  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  WiFi.softAP(ssid, password);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();   // listen for incoming clients

  if (client) {                             // if you get a client,
    Serial.println("New Client.");           // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            // the content of the HTTP response follows the header:
            client.print("Activation des moteurs lorsque le RH du sol est en dessous 50%.<br>");
            client.print("Désactivation des moteurs lorsque le RH du sol est au dessus de 50%.<br>");

            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            break;
          } else {    // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
        // Fonctionne selon TGETSOETUDES+OUVRE ou FERME //
        if (currentLine.endsWith("GET /TGETSOETUDESOUVRE")) {
          digitalWrite(LED_BUILTIN, HIGH);               // DEL de la carte s'allume lorsque la valve ouvre
          digitalWrite(LED_PRIME,HIGH);
        }
        if (currentLine.endsWith("GET /TGETSOETUDESFerme")) {
          digitalWrite(LED_BUILTIN, LOW);                // DEL de la carte s'éteint lorsque la valve ferme
          digitalWrite(LED_PRIME, LOW);
        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
  }
}

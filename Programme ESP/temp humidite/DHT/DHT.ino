#include "DHTesp.h"
#include <ESP8266WiFi.h>
#include <WebSocketServer.h>
#ifdef ESP32
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif

DHTesp dht;
WiFiServer server(80);
WebSocketServer webSocketServer;
 
char* ssid = "TP-LINK_FA18";
char* password =  "Lesduchaussoy";


void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password); 
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
    Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
  
  Serial.println("Status\tHumidity (%)\tTemperature (C)\t(F)\tHeatIndex (C)\t(F)");
  String thisBoard= ARDUINO_BOARD;
  Serial.println(thisBoard);

  // Autodetect is not working reliable, don't use the following line
  // dht.setup(17);
  // use this instead: 
  dht.setup(02, DHTesp::DHT11); // Connect DHT sensor to GPIO 17
  
  server.begin();
  delay(100);
  
}

void loop() {
  
  WiFiClient client = server.available();
 
  if (client.connected() && webSocketServer.handshake(client)) {

    String data;
    int humidity = dht.getHumidity();
    char humidite[8]; // Buffer big enough for 7-character float
    dtostrf(humidity, 6, 2, humidite);
    int temperature = dht.getTemperature();
    char temp[8]; // Buffer big enough for 7-character float
    dtostrf(temperature, 6, 2, temp);
    int resenti = dht.computeHeatIndex(temperature, humidity, false);  
    char tempresenti[8]; // Buffer big enough for 7-character float
    dtostrf(resenti, 6, 2, tempresenti);    
 
    while (client.connected()) {
 
      data = webSocketServer.getData();
 
      if (data == "0"){
        Serial.print("0");
        Serial.println(humidite);
         webSocketServer.sendData(humidite);
      }

      if (data == "1"){
        Serial.print("0");
        Serial.println(temp);
        webSocketServer.sendData(temp);
      }
      if (data == "2"){
        Serial.print("0");
        Serial.println(tempresenti);
        webSocketServer.sendData(tempresenti);
      }
 
      delay(10); // Delay needed for receiving the data correctly
   }
 
   Serial.println("The client disconnected");
   delay(100);
  }
 
  delay(100);
  
}

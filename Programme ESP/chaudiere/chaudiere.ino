#include <ESP8266WiFi.h>
#include <WebSocketServer.h>

//declaration sortie relais D1 D2
int relais_1 =5;
int relais_2= 4;
 
WiFiServer server(80);
WebSocketServer webSocketServer;
 
char* ssid = "TP-LINK_FA18";
char* password =  "Lesduchaussoy";



void setup() {

  pinMode(relais_1, OUTPUT);
  pinMode(relais_2, OUTPUT);
  digitalWrite(relais_1, LOW);
  digitalWrite(relais_2, LOW);
  
  Serial.begin(115200);
 
  WiFi.begin(ssid, password); 
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
 
  server.begin();
  delay(100);
}
 
void loop() {
 
  WiFiClient client = server.available();
 
  if (client.connected() && webSocketServer.handshake(client)) {
 
    String data;      
 
    while (client.connected()) {
 
      data = webSocketServer.getData();
 
      if (data.length() > 0) {
         Serial.println(data);
         webSocketServer.sendData("recu");
      }

      if (data == "1"){
        Serial.println("sortie");
        digitalWrite(relais_1, HIGH);
        digitalWrite(relais_2, HIGH); 
      }
      if (data == "0"){
        digitalWrite(relais_1, LOW);
        digitalWrite(relais_2, LOW);
      }
 
      delay(10); // Delay needed for receiving the data correctly
   }
 
   Serial.println("The client disconnected");
   delay(100);
  }
 
  delay(100);
}

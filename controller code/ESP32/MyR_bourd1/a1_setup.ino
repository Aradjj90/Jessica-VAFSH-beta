
void setup() {
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2);

   WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
 
 

   // Дані для отримання
  // Register for a callback function that will be called when data is received
  esp_now_register_recv_cb(OnDataRecv); 
  delay(100);
}

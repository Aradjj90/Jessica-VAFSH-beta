void setup() {
  Serial.begin(115200);

  pinMode(2, OUTPUT);
// Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  //Дані для відправки 3 платам
  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_register_send_cb(OnDataSent);
  
  // Register peer
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
  
  memcpy(peerInfo.peer_addr, broadcastAddress1, 6);        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }

   memcpy(peerInfo.peer_addr, broadcastAddress2, 6);        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }
  /*
   memcpy(peerInfo.peer_addr, broadcastAddress2, 6);        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }
  */
// Дані для отримання
  // Register for a callback function that will be called when data is received
  esp_now_register_recv_cb(OnDataRecv); 

  
}

void checkfoo(){
 count = 0;
  for (byte i = 0; i<3; i++){
      count += digitalRead(sensorLight);
      delay(200);
    }
}

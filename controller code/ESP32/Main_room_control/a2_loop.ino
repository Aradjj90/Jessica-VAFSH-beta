void loop() {
 
if(save_data.command_one && light_flag){
  comand_light_ON = true;
  light_flag = false;
  bug_timer = millis();
}
if(!save_data.command_one && light_flag){
  comand_light_OFF = true;
  light_flag = false;
  bug_timer = millis();
}



// * **********Automode Sender data*******

if(save_data.command_five)digitalWrite (signalToAr, HIGH);
 else digitalWrite (signalToAr, LOW);

 //save_data.light_automode = 1;
if(save_data.command_five && !flagautomode){
 checkfoo();
  if((count/3) < 1){
  ledcWrite(ledChannel, 101);
  flag_timer = millis();
  bug_timer = millis();
  flagautomode = true;
  switchOff = true;
  Serial.println("Авто мод, світло офф");
}else{
  ledcWrite(ledChannel, 164);
  flag_timer = millis();
  bug_timer = millis();
  flagautomode = true;
  switchOn = true;
  Serial.println("Авто мод, світло он");
}
}
if(flagautomode && millis() -  flag_timer > 1500){
  ledcWrite(ledChannel, 255);
  flag_timer = millis();
  Serial.println("True");
}
if(!save_data.command_five && flagautomode){
  ledcWrite(ledChannel, 1);
  flagautomode=false;
  Serial.println("all off");
}


 //* **********Automode Receiver data*********
 
 
 
sigbal = digitalRead(signalFromAr);
//Serial.println(sigbal);

if(sigbal && switchOn && save_data.command_five && millis() - bug_timer > 800){
   bug_timer = millis();
  comand_light_ON = true;
  Serial.println("Light ON");
  switchOn = false;
  switchOff = true;
}
// переписати
if(!sigbal && switchOff && save_data.command_five && millis() - bug_timer > 800){
   bug_timer = millis();
   comand_light_OFF = true;
   Serial.println("Light OFF");
  switchOff = false;
  switchOn = true;
}


// ******** Керування (ON/OFF) світлом**********

if (comand_light_ON){
    checkfoo();
    if((count/3) < 1){
      releST= !releST;
        digitalWrite (pinReleLight,releST);
        comand_light_ON= false;
        light_ON = true;
        bug_timer = millis(); 
    }
}
if(comand_light_ON && millis() - bug_timer > 4000){
  comand_light_ON = false;
}

 if(light_ON && !light_OFF && millis() - bug_timer > 2000){
  light_ON = false;
  checkfoo();
    if((count/3) < 1){
      releST= !releST;
      digitalWrite (pinReleLight,releST);
    }
}

if (comand_light_OFF){
    checkfoo();
    if((count/3) == 1){
       releST= !releST;
        digitalWrite (pinReleLight,releST);
        comand_light_OFF= false;
        light_OFF = true;
        bug_timer = millis(); 
    }
 }
 
if(comand_light_OFF && millis() - bug_timer > 4000){
  comand_light_OFF = false;
}

if(light_OFF && !light_ON && millis() - bug_timer > 4200){
  light_OFF = false;
  checkfoo();
    if((count/3) == 1){
      releST= !releST;
      digitalWrite (pinReleLight,releST);
    }
}  
}

void checkfoo(){
 count = 0;
  for (byte i = 0; i<3; i++){
      count += digitalRead(sensorLight);
      delay(200);
    }
}

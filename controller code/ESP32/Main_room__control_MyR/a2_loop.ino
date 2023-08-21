
void loop() {
 if(Serial.available()) {
      int val = Serial.parseInt();
      switch (val) {
         case 0: 
        comand_light_OFF = true;
        break;
         case 1: 
        comand_light_ON = true;
        break;
        case 2: 
        Serial2.print("1"); // нічник
        Serial.println("нічник");
        break;
        case 3: 
        Serial2.print("2"); // зміна режимів світла
        break;
        case 4: 
        Serial2.print("3"); // on/off підсвідка
        break;
       
      }
 }

ir_comand(); // IR сигнали
//Serial.println( digitalRead(signalFromAr));
//Serial.println(digitalRead(sensorLight));
//if(save_data.light_automode && fromAr)
//ledcWrite(ledChannel, 101);
if(save_data_main.command_one && light_flag){
  comand_light_ON = true;
  light_flag = false;
   bug_timer = millis();
}
if(!save_data_main.command_one && light_flag){
  comand_light_OFF = true;
  light_flag = false;
   bug_timer = millis();
}

// * **********Automode Sender data*******

if(save_data_main.command_five)digitalWrite (signalToAr, HIGH);
 else digitalWrite (signalToAr, LOW);

 //save_data.light_automode = 1;
if(save_data_main.command_five && !flagautomode){
 checkfoo();
  if((count/3) < 1){
  ledcWrite(ledChannel, 101);
  flag_timer = millis();
  flagautomode = true;
  Serial.println("Авто мод, світло офф");
}else{
  ledcWrite(ledChannel, 164);
  flag_timer = millis();
  flagautomode = true;
  Serial.println("Авто мод, світло он");
}
}
if(flagautomode && millis() -  flag_timer > 1500){
  ledcWrite(ledChannel, 255);
  flag_timer = millis();
  Serial.println("True");
}
if(!save_data_main.command_five && flagautomode){
  ledcWrite(ledChannel, 1);
  flagautomode=false;
  Serial.println("all off");
}


 //* **********Automode Receiver data*********
 
 
 
sigbal = digitalRead(signalFromAr);
//Serial.println(sigbal);
if(sigbal && !switchOn && save_data_main.command_five && millis() - bug_timer > 1300){
  comand_light_ON = true;
  bug_timer = millis();
  Serial.println("Light ON");
  switchOn = true;
  switchOff = false;
}
if(!sigbal && !switchOff && save_data_main.command_five && millis() - bug_timer > 1300){
   comand_light_OFF = true;
   bug_timer = millis();
   Serial.println("Light OFF");
  switchOff = true;
  switchOn = false;
}

// ******** Керування (ON/OFF) світлом **********

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

 if(light_ON && !light_OFF && millis() - bug_timer > 2000){ // змінено
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

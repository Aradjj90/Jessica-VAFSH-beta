void ir_comand(){
if(ir_flag){
  
  if(save_data_main.command_two != check_data_main.command_two){
    Serial2.print("1");
    Serial.println("Нічник");
    check_data_main.command_two = save_data_main.command_two;
  }
  
  if(save_data_main.command_three != check_data_main.command_three){
      Serial2.print("2");
      Serial.println("Зміна світла");
     check_data_main.command_three = save_data_main.command_three;
  }
  
  if(save_data_main.command_four != check_data_main.command_four){
      Serial2.print("3");
      Serial.println("Підсвідка");
     check_data_main.command_four = save_data_main.command_four;
  }
  
  if(save_data_main.command_six != check_data_main.command_six){
      Serial2.print("4");
      Serial.println("Яскравість +");
     check_data_main.command_six = save_data_main.command_six;
  }
  
  if(save_data_main.command_seven != check_data_main.command_seven){
      Serial2.print("5");
      Serial.println("Яскравість -");
     check_data_main.command_seven = save_data_main.command_seven;
  }
  
  if(save_data_main.command_eight != check_data_main.command_eight){
      Serial2.print("6");
      Serial.println("До гарячого");
     check_data_main.command_eight = save_data_main.command_eight;
  }
  
  if(save_data_main.command_nine != check_data_main.command_nine){
      Serial2.print("7");
      Serial.println("До холодного");
     check_data_main.command_nine = save_data_main.command_nine;
  }
}
ir_flag = false;
}

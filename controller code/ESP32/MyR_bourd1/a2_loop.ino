
void loop() {
  if(send_flag){
    
   if(save_data.command_one != massage.command_one){
    Serial2.print("1");
    massage.command_one = save_data.command_one;
  }
     if(save_data.command_two != massage.command_two){
    Serial2.print("2");
    massage.command_two = save_data.command_two;
  }
  
  if(save_data.command_three != massage.command_three){
      Serial2.print("3");
     massage.command_three = save_data.command_three;
  }
  
  if(save_data.command_four != massage.command_four){
      Serial2.print("4");
     massage.command_four = save_data.command_four;
  }
      if(save_data.command_five != massage.command_five){
      Serial2.print("5");
     massage.command_five = save_data.command_five;
  }
   if(save_data.command_six != massage.command_six){
      Serial2.print("6");
     massage.command_six = save_data.command_six;
  }
   if(save_data.command_seven != massage.command_seven){
      Serial2.print("7");
     massage.command_seven = save_data.command_seven;
  }
   if(save_data.command_eight != massage.command_eight){
      Serial2.print("8");
     massage.command_eight = save_data.command_eight;
  }
   if(save_data.command_nine != massage.command_nine){
      Serial2.print("9");
     massage.command_nine = save_data.command_nine;
  }
   if(save_data.command_eleven != massage.command_eleven){
      Serial2.print("11");
     massage.command_eleven = save_data.command_eleven;
  }
   if(save_data.command_twelve != massage.command_twelve){
      Serial2.print("12");
     massage.command_twelve = save_data.command_twelve;
  }
   if(save_data.command_thirteen != massage.command_thirteen){
      Serial2.print("13");
     massage.command_thirteen = save_data.command_thirteen;
  }
   if(save_data.command_fourteen != massage.command_fourteen){
      Serial2.print("14");
     massage.command_fourteen = save_data.command_fourteen;
  }
   if(save_data.command_fiveteen != massage.command_fiveteen){
     if(save_data.command_fiveteen == 1)Serial2.print("15");
     if(save_data.command_fiveteen == 0)Serial2.print("16");
     massage.command_fiveteen = save_data.command_fiveteen;
  }
  


    send_flag = false;
  }
}

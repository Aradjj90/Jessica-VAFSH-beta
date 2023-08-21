
void loop(){
  
  if (Serial.available()) {
    char buf[70];
    int num = Serial.readBytesUntil(';', buf, 70);
    buf[num] = NULL;
    Parser data(buf, ',');
    int ints[20];
   data.parseInts(ints);
    //Serial.print(buf);// повернення даних
   

    switch (ints[0]) {
     
      case 0: // мамина кімната
        massage.command_one = ints[1];       // light_in_room
        massage.command_five = ints[2];      // light_automode
        esp_now_send (broadcastAddress1, (uint8_t *) &massage, sizeof(massage));
        break;
       case 1: // моя кімната
        massage.command_one = ints[1];       // light_in_room
        massage.command_five = ints[2];      // light_automode
        massage.command_two = ints[3];       // nightlight
        massage.command_three = ints[4];     // light_modes
        massage.command_four = ints[5];      // back_light
        massage.command_six = ints[6];       // brightness_plus
        massage.command_seven = ints[7];     // brightness_minus
        massage.command_eight = ints[8];     // movement_to_heat
        massage.command_nine = ints[9];      // movement_to_cold
        massage.command_ten = ints[10];      // switch_board
        esp_now_send (broadcastAddress2, (uint8_t *) &massage, sizeof(massage));
        break;
       case 2: // зал
      
        break;
       case 3: // коридор
      
        break;
       case 4: // кухня
      
        break; 
       case 5: //туалет
      
        break;
        case 6: // моя кімната 2
         massage.command_one = ints[1];        // tv_onoff
         massage.command_two = ints[2];        // tv_source
         massage.command_three = ints[3];      // tv_menu_up
         massage.command_four = ints[4];       //tv_menu_down
         massage.command_five = ints[5];       // tv_menu_ok
         massage.command_six = ints[6];        // tv_menu_5_up
         massage.command_seven = ints[7];      // tv_menu_5_down
         massage.command_eight = ints[8];      // 2_rolls_down
         massage.command_nine = ints[9];       // 2_rolls_up
         massage.command_ten = ints[10];       //switch_board
         massage.command_eleven = ints[11];    // right_roll_down 
         massage.command_twelve = ints[12];    // right_roll_up 
         massage.command_thirteen = ints[13];  // left_roll_down    
         massage.command_fourteen = ints[14];  // left_roll_up 
         massage.command_fiveteen = ints[15];  // table_lamp 
        esp_now_send (broadcastAddress2, (uint8_t *) &massage, sizeof(massage));
        break;

    }

    
  }

}

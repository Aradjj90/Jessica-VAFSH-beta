
#define RXD2 16
#define TXD2 17

#include <esp_now.h>
#include <WiFi.h>

boolean send_flag;

typedef struct struct_message {
   boolean command_one;               //  tv_onoff
    boolean command_two;               // tv_source
    boolean command_three;             // tv_menu_up
    boolean command_four;              // tv_menu_down
    boolean command_five;              // tv_menu_ok
    byte command_six;                  // tv_menu_5_up
    byte command_seven;                // tv_menu_5_down
    byte command_eight;                // 2_rolls_down
    byte command_nine;                 // 2_rolls_up
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
} struct_message;


typedef struct struct_incoming_message {
   boolean command_one;               // tv_onoff
    boolean command_two;               // tv_source
    boolean command_three;             // tv_menu_up
    boolean command_four;              // tv_menu_down
    boolean command_five;              // tv_menu_ok
    byte command_six;                  // tv_menu_5_up
    byte command_seven;                // tv_menu_5_down
    byte command_eight;                // 2_rolls_down
    byte command_nine;                 // 2_rolls_up
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
} struct_incoming_message;

//Структура для зберігання даних
typedef struct struct_save_data {
   boolean command_one;               // tv_onoff
    boolean command_two;               // tv_source
    boolean command_three;             // tv_menu_up
    boolean command_four;              // tv_menu_down
    boolean command_five;              // tv_menu_ok
    byte command_six;                  // tv_menu_5_up
    byte command_seven;                // tv_menu_5_down
    byte command_eight;                // 2_rolls_down
    byte command_nine;                 // 2_rolls_up
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
} struct_save_data;

struct_message massage;
struct_incoming_message incoming_message;
struct_save_data save_data;


esp_now_peer_info_t peerInfo;




// Callback when data is received
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incoming_message, incomingData, sizeof(incoming_message));  
  save_data.command_one = incoming_message.command_one;
  save_data.command_two = incoming_message.command_two;
  save_data.command_three = incoming_message.command_three;
  save_data.command_four = incoming_message.command_four;
  save_data.command_five = incoming_message.command_five;
  save_data.command_six = incoming_message.command_six;
  save_data.command_seven = incoming_message.command_seven;
  save_data.command_eight = incoming_message.command_eight;
  save_data.command_nine = incoming_message.command_nine;
  save_data.command_eleven = incoming_message.command_eleven;
  save_data.command_twelve = incoming_message.command_twelve;
  save_data.command_thirteen = incoming_message.command_thirteen;
  save_data.command_fourteen = incoming_message.command_fourteen;
  save_data.command_fiveteen = incoming_message.command_fiveteen;
  send_flag = true;
}

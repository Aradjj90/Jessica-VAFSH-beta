#include <Parser.h>
#include <esp_now.h>
#include <WiFi.h>

//                           E1

// адреса приймачів
uint8_t broadcastAddress1[] = {0xF0, 0x08, 0xD1, 0xD2, 0x89, 0x50};//мамина кімната
uint8_t broadcastAddress2[] = {0xAC, 0x67, 0xB2, 0x34, 0xF9, 0xB0};//моя кімната

//Структура для зберігання даних
typedef struct struct_save_data {       // Myroom       // Mamroom
    boolean command_one;               // light_in_room // tv_onoff
    boolean command_two;               // nightlight // tv_source
    boolean command_three;             // light_modes // tv_menu_up
    boolean command_four;              // back_light // tv_menu_down
    boolean command_five;              // light_automode // tv_menu_ok
    byte command_six;                  // brightness_plus // tv_menu_5_up
    byte command_seven;                // brightness_minus // tv_menu_5_down
    byte command_eight;                // movement_to_heat // 2_rolls_down
    byte command_nine;                 // movement_to_cold // 2_rolls_up
    byte command_ten;                  // switch_board
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
    
} struct_save_data;

//Тип структури для відправки
typedef struct struct_message{           // Myroom  // Mamroom
    boolean command_one;               // light_in_room // tv_onoff
    boolean command_two;               // nightlight // tv_source
    boolean command_three;             // light_modes // tv_menu_up
    boolean command_four;              // back_light // tv_menu_down
    boolean command_five;              // light_automode // tv_menu_ok
    byte command_six;                  // brightness_plus // tv_menu_5_up
    byte command_seven;                // brightness_minus // tv_menu_5_down
    byte command_eight;                // movement_to_heat // 2_rolls_down
    byte command_nine;                 // movement_to_cold // 2_rolls_up
    byte command_ten;                  // switch_board
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
} struct_message;

typedef struct struct_incoming_message { // Myroom      // Mamroom
    boolean command_one;               // light_in_room // tv_onoff
    boolean command_two;               // nightlight // tv_source
    boolean command_three;             // light_modes // tv_menu_up
    boolean command_four;              // back_light // tv_menu_down
    boolean command_five;              // light_automode // tv_menu_ok
    byte command_six;                  // brightness_plus // tv_menu_5_up
    byte command_seven;                // brightness_minus // tv_menu_5_down
    byte command_eight;                // movement_to_heat // 2_rolls_down
    byte command_nine;                 // movement_to_cold // 2_rolls_up
    byte command_ten;                  // switch_board 
    byte command_eleven;               // right_roll_down 
    byte command_twelve;               // right_roll_up 
    byte command_thirteen;             // left_roll_down 
    byte command_fourteen;             // left_roll_up 
    byte command_fiveteen;             // table_lamp 
} struct_incoming_message;


//оголошення структур
struct_message massage;
struct_save_data save_data;
struct_incoming_message incoming_message;

esp_now_peer_info_t peerInfo;


// Callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}

 void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incoming_message, incomingData, sizeof(incoming_message));  
 }

 



/********** Communication protocol **********
 * 
 *              [0,1,2,3,4,5]
 *              
 *                 For Receiver
 *  0 - кімната з якої відправлена комада ints[0] - (0/10)
 *  1 - команда включити чи виключити світло - (0/1)
 *  2 - вкл./вк. режим автоматичного контролю світла - (0/1)
 * 
 * 
 *                               Е1
 */

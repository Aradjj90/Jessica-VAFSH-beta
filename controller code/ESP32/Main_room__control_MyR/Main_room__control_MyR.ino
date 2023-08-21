/*
 ESP 32 DEV KID - контролер біля розподільчої коробки. 
GPIO USE

13 - реле світла 
23 - сенсорна кнопка на виключателі *** (жовтий дріт - нижній датчик)
22 - сенсорна кнопка на виключателі *** (зелений дріт - верхній датчик)
4 - дачик електрики
27 - прийом сигналу від Ардуино в дверях
26 - відправка сигналу до Ардуино в дверях

*/

/*
                            On Test
_____________________________________________________________



               
 
*/


#define pinReleLight 13
#define sensorButtenUp 22 
#define sensorButtenDwon 23
#define sensorLight 4
#define signalFromAr 27
#define signalToAr 26

#define RXD2 16
#define TXD2 17 // відправник

#include <esp_now.h>
#include <WiFi.h>


boolean light_ON,light_OFF, comand_light_ON, comand_light_OFF, releST, light, light_flag;
boolean fromAr, toAr, switchOn,switchOff,sigbal, flagautomode, ir_flag;
unsigned long bug_timer,flag_timer;
float count;
byte diligence;

const int freq = 490;
const int ledChannel = 0;
const int resolution = 8;

// адреса приймачів
uint8_t broadcastAddress1[] = {0x10, 0x52, 0x1C, 0x5D, 0xFA, 0xFC};//E2
//uint8_t broadcastAddress2[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};


//Структура для зберігання даних
typedef struct struct_save_data_main {
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
} struct_save_data_main;


typedef struct struct_check_data_main {
   boolean command_one;               // light_in_room // tv_onoff
    boolean command_two;               // nightlight // tv_source
    boolean command_three;             // light_modes // tv_menu_up
    boolean command_four;              // back_light // tv_menu_down
    boolean command_five;              // light_automode // tv_menu_ok
    byte command_six;                  // brightness_plus // tv_menu_5_up
    byte command_seven;                // brightness_minus // tv_menu_5_down
    byte command_eight;                // movement_to_heat // 2_rolls_down
    byte command_nine;                 // movement_to_cold // 2_rolls_up
} struct_check_data_main;


//Тип структури для відправки
typedef struct struct_message {
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

typedef struct struct_incoming_message {
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
struct_incoming_message incoming_message;
struct_save_data_main save_data_main;
struct_check_data_main check_data_main;



esp_now_peer_info_t peerInfo;


// Callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
  
}

// Callback when data is received
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incoming_message, incomingData, sizeof(incoming_message));  
   Serial.println("done");
   Serial.println(incoming_message.command_ten);
  if(!incoming_message.command_ten){
  save_data_main.command_one = incoming_message.command_one;
  save_data_main.command_two = incoming_message.command_two;
  save_data_main.command_three = incoming_message.command_three;
  save_data_main.command_four = incoming_message.command_four;
  save_data_main.command_five = incoming_message.command_five;
  save_data_main.command_six = incoming_message.command_six;
  save_data_main.command_seven = incoming_message.command_seven;
  save_data_main.command_eight = incoming_message.command_eight;
  save_data_main.command_nine = incoming_message.command_nine;
  light_flag = true; //  відкриває доступ до функцій переключення світла
  ir_flag = true;
  Serial.println("first");
  }else{
  massage.command_one = incoming_message.command_one;
  massage.command_two = incoming_message.command_two;
  massage.command_three = incoming_message.command_three;
  massage.command_four = incoming_message.command_four;
  massage.command_five = incoming_message.command_five;
  massage.command_six = incoming_message.command_six;
  massage.command_seven = incoming_message.command_seven;
  massage.command_eight = incoming_message.command_eight;
  massage.command_nine = incoming_message.command_nine;
  massage.command_eleven = incoming_message.command_eleven;
  massage.command_twelve = incoming_message.command_twelve;
  massage.command_thirteen = incoming_message.command_thirteen;
  massage.command_fourteen = incoming_message.command_fourteen;
  massage.command_fiveteen = incoming_message.command_fiveteen;
  esp_now_send (broadcastAddress1, (uint8_t *) &massage, sizeof(massage));
  Serial.println("send");
  }
  
 // save_data.command_duplication = incoming_message.command_duplication;
}

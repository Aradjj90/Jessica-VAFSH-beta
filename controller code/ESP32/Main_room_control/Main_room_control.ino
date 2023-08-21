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

- Загальна управляюча програма
- відправка 3 платам дані 
- прийом даних 

               E2
 
*/
// Треба написати функцію для перевірки струму

#define pinReleLight 13
#define sensorButtenUp 22 
#define sensorButtenDwon 23
#define sensorLight 4 
#define signalFromAr 27
#define signalToAr 26

#include <esp_now.h>
#include <WiFi.h>

boolean light_ON,light_OFF, comand_light_ON, comand_light_OFF, releST, light, light_flag;
boolean fromAr, toAr, switchOn,switchOff,sigbal, flagautomode;
unsigned long bug_timer,flag_timer;
float count;
byte diligence;

const int freq = 490;
const int ledChannel = 0;
const int resolution = 8;

// адреса приймачів
uint8_t broadcastAddress1[] = {0xF0, 0x08, 0xD1, 0xD2, 0xA4, 0x80};//E1
//uint8_t broadcastAddress2[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};


//Структура для зберігання даних
typedef struct struct_save_data {
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
struct_save_data save_data;

esp_now_peer_info_t peerInfo;


// Callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
  
}

// Callback when data is received
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incoming_message, incomingData, sizeof(incoming_message));
  
  save_data.command_one = incoming_message.command_one;
  save_data.command_five = incoming_message.command_five;
  light_flag = true; //  відкриває доступ до функцій переключення світла
 // save_data.command_duplication = incoming_message.command_duplication;
}

 

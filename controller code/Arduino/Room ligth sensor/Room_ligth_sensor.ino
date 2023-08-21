// Arduino в дверях ( міряє освітлення в кімнати 
// - міряє освітлення в кімнати 
// - робить дитекцію хто зайшов в кімнату
// - передає дани на ESP 32


/*
 * Настройка датчиків 
 *         Моя кімната 
 *   IN  - !sen1dt && sen2dt   
 *   OUT -  sen1dt && !sen2dt
 *   
 *         Мамина кімната
 *   OUT  - !sen1dt && sen2dt   
 *   IN   -  sen1dt && !sen2dt
 * 
 */

#define pinSensor1 4
#define pinSensor2 6
#define signalFromESP 9
#define signalToESP 10
#define gmdForFoto 7
#define vinForFoto 8


#define RIGHT_SIDE // напрямок включання світла(якщо опреділено, то рух направо включить світло)


#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor1;
VL53L0X sensor2;

int sen1, sen2, sensorval;
boolean sen1dt, sen2dt, in, out, automode;
int fromESP;
byte countdt1,countdt2, person;
unsigned long timeout1, timeout2, timeoutlight, timeout;




void setup() {
  Serial.begin(115200);
  pinMode(signalFromESP,INPUT);//з esp32 до ардуино ( 4Ж зелений з білим)(8Ж коричневий з білим)
  pinMode(signalToESP,OUTPUT);// передача даних до esp32 (4Ж синій з білим)(8Ж помаранчевий з білим)
  pinMode(vinForFoto,OUTPUT); // Живлення для фоторезистора
  pinMode(gmdForFoto,OUTPUT); // Земля для датчика світла
  pinMode(pinSensor2,OUTPUT); // контроль одного з датчиків
  pinMode(pinSensor1,OUTPUT); // контроль одного з датчиків
  digitalWrite(vinForFoto,HIGH); 
  digitalWrite(gmdForFoto,LOW);
  digitalWrite(pinSensor1,LOW);
  digitalWrite(pinSensor2,LOW);
 delay(500);

Wire.begin();

Serial.println("sen1, sen2, light");
digitalWrite(pinSensor1, HIGH);
delay(150);
sensor1.setTimeout(500);
sensor1.init(true);
delay(100);
sensor1.setAddress((uint8_t)01);

digitalWrite(pinSensor2, HIGH);
delay(150);
sensor2.setTimeout(500);
sensor2.init(true);
delay(100);
sensor2.setAddress((uint8_t)02);


//Serial.println("addresses set");

 sensor1.setMeasurementTimingBudget(20000);
 sensor2.setMeasurementTimingBudget(20000);
//sensor1.startContinuous();
//sensor2.startContinuous();  

}

void loop() {
  
  /*
 * **********Automode Receiver data**********
 */
 
fromESP=(pulseIn(signalFromESP, HIGH)); // 255 на ESP на прийоми 2020

//fromESP=digitalRead(signalFromESP);




Serial.println(fromESP);
/*
if(fromESP){
  automode =true;
  person = 0;
}
else automode =false;
*/

if(fromESP < 200){
  automode = false;
  digitalWrite(signalToESP, LOW);
  Serial.println("Automode OFF");
}
if(fromESP > 300 && fromESP <700){ // 101 на стороні ESP 32
  automode =true;
  person = 0;
  Serial.println("Automode ON, Light OFF");
}
if(fromESP > 1200 && fromESP <1500){ // 164 на стороні ESP 32
  automode =true;
  person = 1;
  Serial.println("Automode ON, Light ON");
}
if(fromESP > 1900)automode =true;



if(person>3 || person ==0 && (millis() - timeoutlight >10000 && automode)){
    digitalWrite(signalToESP, LOW);
    person = 0;
  }
  if(person>0 && automode)digitalWrite(signalToESP, HIGH);


 
/*
 * ********** IR Sensor read *********
 */



//Serial.print(sen1);
//Serial.print("-");
//Serial.println(sen2);

if(sen1<500 && !sen1dt && automode ){
  countdt1++;
  if(countdt1==3 && !sen1dt){
    sen1dt = true;
    timeout1 = millis();
  }
}

if(sen2<500 && !sen2dt && automode){
  countdt2++;
  if(countdt2==3 && !sen2dt){
    sen2dt = true;
    timeout2 = millis();
  }
}

 // змінити в умові місцями якщо інша кімната sen2dt на sen1dt
if(sen2dt && in){
  person++;
  sen2dt = false;
  sen1dt = false;
  countdt2 =0;
  countdt1 =0;
  out = false;
  in=false;
  timeoutlight =  millis();
}
// змінити в умові місцями якщо інша кімната sen2dt на sen1dt і навпаки
if(sen1dt && out){
  person--;
  sen2dt = false;
  sen1dt = false;
  countdt2 =0;
  countdt1 =0;
  out = false;
  in=false;
  timeoutlight =  millis();
}
// змінити в перезапісі місцями якщо інша кімната in на out і навпаки
if(sen1dt && !sen2dt){
  in = true;
  
}
if(!sen1dt && sen2dt){
  out = true;
  
}

if (sen1dt && sen2dt && !out && !in){
  sen2dt = false;
  sen1dt = false;
  countdt2 =0;
  countdt1 =0;
}

// Перевірити

if(sen1dt && (millis() - timeout1 > 2000)){
  sen1dt = false;
  sen2dt = false;
  countdt2 =0;
  countdt1 =0;
}
if(sen2dt && (millis() - timeout2 > 2000)){
  sen1dt = false;
  sen2dt = false;
  countdt2 =0;
  countdt1 =0;
}

//Serial.println(person);
//Serial.print("Aoutomode = ");
//Serial.println(automode);

}
int filterSignal(int pin, int samples){
  // переменная для хранения суммы считанных значений
  int sum = 0;
  // чтение и складывание значений
  for (int i = 0; i < samples; i++){
    sum = sum + analogRead(pin);
  }
  // делим сумму значений на количество измерений
  sum = sum/samples;
  // возвращаем среднее значение
  return sum;
}

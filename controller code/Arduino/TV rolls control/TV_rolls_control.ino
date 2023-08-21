#define Mosfet 13
#define counter 6144
#define dl 2

#include <IRremote.h> 
#include <MYButton.h>
#include <AccelStepper.h>
#include <MultiStepper.h>

const float STEPS_PER_OUT_REV = 2048;
long positions[2];
int serialData, togo;
//The sequence 1-3-2-4 is required for proper sequencing of 28BYJ48
IRsend irsend;
MYButton dtcholL(12);
MYButton dtcholR(2);
AccelStepper stepper1(AccelStepper::FULL4WIRE, 4, 5, 6, 7);// Right
AccelStepper stepper2(AccelStepper::FULL4WIRE, 8, 9, 10, 11);// Left 
MultiStepper steppers;

void setup(){
  Serial.begin(115200);
  Serial.setTimeout(10);
  stepper1.setMaxSpeed(350);
  stepper2.setMaxSpeed(350);
  stepper1.setAcceleration(150);
  stepper2.setAcceleration(150);
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
  pinMode(Mosfet, OUTPUT);
  digitalWrite(Mosfet, LOW);
  steperToRef(stepper1,dtcholR, 4,5,6,7);
  steperToRef(stepper2,dtcholL, 8,9,10,11);
}
 
void loop() {
 
     if(Serial.available()) {
      int val = Serial.parseInt();
      Serial.print(val);
      switch (val) {
      case 1:
      irsend.sendNEC(0x40BE629D, 32); // on/off
      break;
      case 2:
      irsend.sendNEC(0x40BED22D, 32); // source
      break;
      case 3:
      irsend.sendNEC(0x40BE12ED, 32); // menu up
      break;
      case 4:
      irsend.sendNEC(0x40BEB24D, 32); // menu down
      break;
      case 5:
      irsend.sendNEC(0x40BE52AD, 32); // menu ok
      break;
      case 6:
      irsend.sendNEC(0x40BE12ED, 32); // menu 5 up
      delay(100);
      irsend.sendNEC(0x40BE12ED, 32);
      delay(100);
      irsend.sendNEC(0x40BE12ED, 32); 
      delay(100);
      irsend.sendNEC(0x40BE12ED, 32);
      delay(100);
      irsend.sendNEC(0x40BE12ED, 32);
      break;
      case 7:
      irsend.sendNEC(0x40BEB24D, 32); // menu 5 Down
      delay(100);
      irsend.sendNEC(0x40BEB24D, 32);
      delay(100);
      irsend.sendNEC(0x40BEB24D, 32);
      delay(100);
      irsend.sendNEC(0x40BEB24D, 32);
      delay(100);
      irsend.sendNEC(0x40BEB24D, 32);
      break;
      case 8: // опуск двох рулетив в низ (базова точка)
       stepper1.setMaxSpeed(400);
        stepper2.setMaxSpeed(400);
       positions[0] +=STEPS_PER_OUT_REV*11;
       positions[1] +=STEPS_PER_OUT_REV*11;
       steppers.moveTo(positions);
       steppers.runSpeedToPosition(); // Blocks until all are in position
       motoroff();
        delay(500);
        break;
        case 9: // підйом двох рулетив вверх
        stepper1.setMaxSpeed(350);
        stepper2.setMaxSpeed(350);
       positions[0] =0;
       positions[1] =0;
       steppers.moveTo(positions);
       steppers.runSpeedToPosition(); // Blocks until all are in position
       motoroff();
        delay(500);
        break;
        case 11: // опустити правий рол
        stepper1.setMaxSpeed(400);
        togo +=STEPS_PER_OUT_REV*11;
        stepper1.runToNewPosition(togo);
        motoroff();
        delay(500);
        break;
        case 12: // підняти правий рол
        stepper1.setMaxSpeed(350);
        togo =0;
        stepper1.runToNewPosition(togo);
        motoroff();
        delay(500);
        break;
        case 13: // опустити лівий рол
        stepper2.setMaxSpeed(400);
        togo +=STEPS_PER_OUT_REV*11;
       stepper2.runToNewPosition(togo);
       motoroff();
        delay(500);
        break;
        case 14: // підняти лівий рол
        stepper2.setMaxSpeed(350);
        togo =0;
       stepper2.runToNewPosition(togo);
       motoroff();
        delay(500);
        break;
         case 15: // включити настільну лампу
        digitalWrite(Mosfet, HIGH);
        delay(500);
        break;
        case 16: // виключити настільну лампу
        digitalWrite(Mosfet, LOW);
        delay(500);
        break;
        
    }
  }

  
} 

 void motoroff(){
  for (byte i = 4; i <= 11; i++) digitalWrite(i, LOW);
 }
 void steperToRef( AccelStepper &stepper,MYButton &button, byte in1, byte in2, byte in3, byte in4){
  for (int i=0;i<=counter;i++){
  
  button.listenButton();
  if(button.isPress()){
    stepper.setCurrentPosition(0);
    stepper.setMaxSpeed(350);
    stepper.setAcceleration(150);
    break;
  }
  //0
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(dl);
//1
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  delay(dl);
//2
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(dl);
  if(button.isPress()){
    stepper.setCurrentPosition(0);
    stepper.setMaxSpeed(350);
    stepper.setAcceleration(150);
    break;
  }
//3
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(dl);
//4
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(dl);
//5
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  delay(dl);
//6
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(dl);
//7
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(dl);
  }
  motoroff();
}

 

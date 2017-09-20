#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int LEFTPIN = 13;
int RIGHTPIN = 12;
int STOP = 1500;
int CLOCKWISE = 1300;
int C_CLOCKWISE = 1700;

void stopServos() {
  servoLeft.writeMicroseconds(STOP);
  servoRight.writeMicroseconds(STOP);
  delay(500);
}

void forward(int time){
  servoLeft.writeMicroseconds(C_CLOCKWISE);
  servoRight.writeMicroseconds(CLOCKWISE);
  delay(time);
}

void backward(int time){
  servoLeft.writeMicroseconds(CLOCKWISE);
  servoRight.writeMicroseconds(C_CLOCKWISE);
  delay(time);
}

void left(){
  servoLeft.writeMicroseconds(CLOCKWISE);
  servoRight.writeMicroseconds(CLOCKWISE);
  delay(600);
  stopServos();
}

void right(){
  servoLeft.writeMicroseconds(C_CLOCKWISE);
  servoRight.writeMicroseconds(C_CLOCKWISE);
  delay(600);
}

void setup() {
  servoLeft.attach(LEFTPIN);
  servoRight.attach(RIGHTPIN);
  stopServos();
}

void loop() {
  for(int i = 0; i < 4; i++) {
    forward(500);
    delay(200);
    backward(500);
  }
  left();
  forward(1000);
  right();
  backward(2000);
  forward(1000);
  right();
  left();
  left();
  right();
  for(int i = 0; i < 4; i++)
  { left(); }
  

}

#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int LEFTPIN = 13;
int RIGHTPIN = 12;
int RIGHTW = 5;
int LEFTW = 7;
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
}

void right(){
  servoLeft.writeMicroseconds(C_CLOCKWISE);
  servoRight.writeMicroseconds(C_CLOCKWISE);
  delay(600);
}

void setup() {
  servoLeft.attach(LEFTPIN);
  servoRight.attach(RIGHTPIN);
  pinMode(RIGHTW, INPUT);
  pinMode(LEFTW, INPUT);
  stopServos();
}

void loop() {
  forward(5);
  if (digitalRead(RIGHTW) == LOW){
    backward(500);
    left();
  }
  if (digitalRead(LEFTW) == LOW) {
    backward(500);
    left();
  }
}

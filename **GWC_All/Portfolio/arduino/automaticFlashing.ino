int LED = 8;
int BUTTON = 7;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT);
}

void loop() {
  
  delay(300);
  if(digitalRead(BUTTON)==HIGH) {
    digitalWrite(LED, HIGH);
  }
  else if(digitalRead(BUTTON)==LOW){
    digitalWrite(LED, LOW);
  }
}

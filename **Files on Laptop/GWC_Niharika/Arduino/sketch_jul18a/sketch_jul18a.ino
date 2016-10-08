int LED_A = 4;
int LED_B = 5;
  
  void setup() {
  pinMode(LED_A, OUTPUT);
  pinMode(LED_B, OUTPUT);
  delay(1000);
}

void loop() {
  digitalWrite(LED_A, HIGH);
  digitalWrite(LED_B, LOW);
  delay(1000);
  digitalWrite(LED_B, HIGH);
  digitalWrite(LED_A, LOW);
  delay(1000);
  //The LED connected to pin 4 is on when the pin 5 LED is off and they blink on for one second, off for one second.

  
  digitalWrite(LED_A, HIGH);
  digitalWrite(LED_A, LOW);
  delay(300);
  digitalWrite(LED_B, HIGH);
  digitalWrite(LED_B, LOW);
  delay(300);
  digitalWrite(LED_A, HIGH);
  digitalWrite(LED_A, LOW);
  delay(300);
  digitalWrite(LED_B, HIGH);
  digitalWrite(LED_B, LOW);
  delay(300);
  digitalWrite(LED_A, HIGH);
  digitalWrite(LED_A, LOW);
  delay(300);
  digitalWrite(LED_B, HIGH);
  digitalWrite(LED_B, LOW);
  delay(300);
  digitalWrite(LED_A, HIGH);
  digitalWrite(LED_A, LOW);
  delay(300);
}

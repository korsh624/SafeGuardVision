void setup() {
  pinMode(13, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String r = Serial.readString();
    if (r == "danger") {
      while (digitalRead(10) == 0) {
        digitalWrite(13, 1);
        analogWrite(9, 125);
        delay(1000);
        digitalWrite(13, 0);
        analogWrite(9, 0);
        delay(1000);
      }
      r = "";
    }
  }
}

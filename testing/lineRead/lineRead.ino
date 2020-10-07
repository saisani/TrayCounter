int pin = 7;
int val;

void setup() {
  pinMode(pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  val = digitalRead(pin);
  Serial.println(val);

}

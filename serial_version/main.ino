char receivedChar;
boolean newData = false;

// -- you can change the pins right here
const int redLed = 4;
const int yellowLed = 2;
const int greenLed = 5;
const int blueLed = 3;

void setup() {
    Serial.begin(9600);
    pinMode(redLed, OUTPUT);
    pinMode(yellowLed, OUTPUT);
    pinMode(greenLed, OUTPUT);
    pinMode(blueLed, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        receivedChar = Serial.read();
        newData = true;
    }

    if (newData) {
        if (receivedChar == 'r') {
            digitalWrite(redLed, HIGH);
            delay(1000);
            digitalWrite(redLed, LOW);
        } else if (receivedChar == 'y') {
            digitalWrite(yellowLed, HIGH);
            delay(1000);
            digitalWrite(yellowLed, LOW);
        } else if (receivedChar == 'g') {
            digitalWrite(greenLed, HIGH);
            delay(1000);
            digitalWrite(greenLed, LOW);
        } else if (receivedChar == 'b') {
            digitalWrite(blueLed, HIGH);
            delay(1000);
            digitalWrite(blueLed, LOW);
        } else if (receivedChar == 'a') {
            digitalWrite(redLed, HIGH);
            digitalWrite(yellowLed, HIGH);
            digitalWrite(greenLed, HIGH);
            digitalWrite(blueLed, HIGH);
            delay(1000);
            digitalWrite(redLed, LOW);
            digitalWrite(yellowLed, LOW);
            digitalWrite(greenLed, LOW);
            digitalWrite(blueLed, LOW);
        }
        newData = false;
    }

    delay(100);
}
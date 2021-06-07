#include <Arduino.h>
#include "Servo.h"

#define SERVO_PIN 13
#define PIN_TRIG 10
#define PIN_ECHO 11

Servo servo;

void setup()
{
	Serial.begin (9600);
	servo.attach(SERVO_PIN);
	servo.write(0);
	pinMode(PIN_TRIG, OUTPUT);
	pinMode(PIN_ECHO, INPUT);
}

uint8_t period = 20;
uint64_t period_start;

uint8_t angle = 0;
uint8_t angle_step = 2;

void uSensor()
{
	double distance;

	digitalWrite(PIN_TRIG, LOW);
	delayMicroseconds(5);
	digitalWrite(PIN_TRIG, HIGH);
	delayMicroseconds(10);
	digitalWrite(PIN_TRIG, LOW);
	distance = (double)pulseIn(PIN_ECHO, HIGH, 17460) / 5820;
	Serial.print(distance);
	Serial.print("   ");
	Serial.println(angle);
}

void loop()
{
	period_start = millis();
	uSensor();


	angle += angle_step;
	if (angle > 180)
	{
		angle_step *= -1;
		angle += 2 * angle_step;
	}
	servo.write(angle);




	while (millis() - period_start < period)
		delay(1);
}

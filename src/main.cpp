#include "robot.h"

uint8_t period = 20;
uint8_t angle = 0;
uint8_t angle_step = 2;

uint64_t period_start;
Servo servo;
String control;

void setup()
{
	Serial.begin (9600);
	servo.attach(SERVO_PIN);
	servo.write(0);
	pinMode(PIN_TRIG, OUTPUT);
	pinMode(PIN_ECHO, INPUT);

	for (int i = 4; i < 8; i++)
	{
		pinMode(i, OUTPUT);
	}
}

void loop()
{
	period_start = millis();
	uSensor();
	Serial.println(angle);

	if (Serial.available())
	{
		control = Serial.readStringUntil('\n');
		if (control == "0")
			stop();
		if (control == "1")
			go_forward();
		if (control == "2")
			go_back();
		if (control == "3")
			turn_right();
		if (control == "4")
			turn_left();
		Serial.println(control);
	}

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

//
// Created by romak on 07.06.2021.
//

#include "robot.h"

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
}

void stop()
{
	analogWrite(SPEED_1, 0);
	analogWrite(SPEED_2, 0);
}

void go_forward()
{
	digitalWrite(DIR_1, HIGH);
	digitalWrite(DIR_2, HIGH);
	analogWrite(SPEED_1, 255);
	analogWrite(SPEED_2, 255);
}

void go_back()
{
	digitalWrite(DIR_1, LOW);
	digitalWrite(DIR_2, LOW);
	analogWrite(SPEED_1, 150);
	analogWrite(SPEED_2, 150);
}

void turn_right()
{
	digitalWrite(DIR_1, HIGH);
	digitalWrite(DIR_2, LOW);
	analogWrite(SPEED_1, 150);
	analogWrite(SPEED_2, 150);
}

void turn_left()
{
	digitalWrite(DIR_1, LOW);
	digitalWrite(DIR_2, HIGH);
	analogWrite(SPEED_1, 150);
	analogWrite(SPEED_2, 150);
}

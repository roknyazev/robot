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

void go_forward(uint8_t &val1, uint8_t &val2, uint8_t &dir1, uint8_t &dir2)
{
	if (dir1  != HIGH || dir2 != HIGH)
	{
		dir1 = HIGH;
		dir2 = HIGH;
		val1 = max(val1, val2);
		val2 = val1;
	}
	if (val1 != 255)
		val1 += STEP;
	if (val2 != 255)
		val2 += STEP;
	digitalWrite(DIR_1, dir1);
	digitalWrite(DIR_2, dir2);
	analogWrite(SPEED_1, val1);
	analogWrite(SPEED_2, val2);
}

void go_back(uint8_t &val1, uint8_t &val2, uint8_t &dir1, uint8_t &dir2)
{
	if (dir1  != LOW || dir2 != LOW)
	{
		dir1 = LOW;
		dir2 = LOW;
		val1 = max(val1, val2);
		val2 = val1;
	}
	if (val1 != 255)
		val1 += STEP;
	if (val2 != 255)
		val2 += STEP;
	digitalWrite(DIR_1, dir1);
	digitalWrite(DIR_2, dir2);
	analogWrite(SPEED_1, val1);
	analogWrite(SPEED_2, val2);
}

void turn_right(uint8_t &val1, uint8_t &val2, uint8_t &dir1, uint8_t &dir2)
{
	if (val1 != 255)
		val1 += STEP;
	if (val2 != 255)
		val2 += STEP;
	digitalWrite(DIR_1, HIGH);
	digitalWrite(DIR_2, LOW);
	analogWrite(SPEED_1, val1);
	analogWrite(SPEED_2, val2);
}

void turn_left(uint8_t &val1, uint8_t &val2, uint8_t &dir1, uint8_t &dir2)
{
	if (val1 != 255)
		val1 += STEP;
	if (val2 != 255)
		val2 += STEP;
	digitalWrite(DIR_1, LOW);
	digitalWrite(DIR_2, HIGH);
	analogWrite(SPEED_1, val1);
	analogWrite(SPEED_2, val2);
}

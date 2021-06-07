//
// Created by romak on 07.06.2021.
//

#ifndef UNTITLED_ROBOT_H
#define UNTITLED_ROBOT_H

#include <Arduino.h>
#include "Servo.h"

#define SPEED_1      5
#define DIR_1        4

#define SPEED_2      6
#define DIR_2        7

#define SERVO_PIN 13
#define PIN_TRIG 10
#define PIN_ECHO 11



void uSensor();
void stop();
void go_forward();
void go_back();
void turn_right();
void turn_left();

#endif //UNTITLED_ROBOT_H

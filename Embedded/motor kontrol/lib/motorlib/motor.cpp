#include "motor.h"
#include "Arduino.h"

#define OUTPUT 1

int DIR;
int STEP;
Motor::Motor(int dir, int step){
  DIR = dir;
  STEP = step;
}

void Motor::mot_begin(){
  pinMode(DIR,OUTPUT);
  pinMode(STEP,OUTPUT);
}
void Motor::mot_write(double degree , bool dir){
  digitalWrite(DIR, dir);
  int a = degree / 1.8;
  for(int i = 0 ; i < a ; i++){
      digitalWrite(STEP, HIGH);
      delayMicroseconds(50);
      digitalWrite(STEP, LOW);
      delayMicroseconds(50);
  }
}
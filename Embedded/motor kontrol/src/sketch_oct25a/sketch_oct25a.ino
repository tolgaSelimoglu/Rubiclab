/*

  Stepper Motor A4988 Driver Example

  No code here - use the pushbutton to rotate a single step, and the switch to control the direction

*/
/*
#define MOT1_DIR 2
#define MOT1_STEP 3

#define MOT2_DIR 4
#define MOT2_STEP 5

#define MOT3_DIR 6
#define MOT3_STEP 7

#define MOT4_DIR 8
#define MOT4_STEP 9
*/

#include <motor.h>
Motor MOT1(2,3);
Motor MOT2(4,5);
Motor MOT3(6,7);
Motor MOT4(7,8);



  


void setup() {
  MOT1.mot_begin();
    MOT2.mot_begin();
      MOT3.mot_begin();
        MOT4.mot_begin();
  delay(1000);
  MOT1.mot_write(90.0, 1);
}
void loop() {

//doksan(MOT1_DIR, MOT1_STEP, 1);

}

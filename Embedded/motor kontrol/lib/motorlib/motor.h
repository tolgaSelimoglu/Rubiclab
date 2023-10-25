#ifndef motor_h
#define motor_h

class Motor{
   public:
    int DIR;
    int STEP;
    Motor(int dir , int step);
    void mot_begin();
    void mot_write(double degree , bool DIR);
};
#endif
#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################
from SR02 import SR02_Supersonic as Supersonic_Sensor

import front_wheels

import rear_wheels

import time

from car import Car


class myCar(object):

    def __init__(self, car_name):

        self.car = Car(car_name)

    def drive_parking(self):

        self.car.drive_parking()

    # =======================================================================

    # 1ST_ASSIGNMENT_CODE

    # Complete the code to perform First Assignment

    # =======================================================================

    def car_startup(self):

        speed = [30, 50, 70]
        dis = [15, 20, 25]

        for i in range(3):
            distance = self.car.distance_detector.get_distance()
            self.car.accelerator.go_forward(speed[i])
            while distance > dis[i] or distance == -1:
                distance = self.car.distance_detector.get_distance()
            self.car.accelerator.stop()
            time.sleep(0.01)
            self.car.accelerator.go_backward(speed[i])
            time.sleep(4)
            self.car.accelerator.stop()
            time.sleep(0.01)
        pass

if __name__ == "__main__":

    try:

        myCar = myCar("CarName")

        myCar.car_startup()



    except KeyboardInterrupt:

        # when the Ctrl+C key has been pressed,

        # the moving object will be stopped

        myCar.drive_parking()
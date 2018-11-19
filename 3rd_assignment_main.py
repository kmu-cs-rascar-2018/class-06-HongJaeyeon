#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from SR02 import SR02_Supersonic as Supersonic_Sensor
import front_wheels
import rear_wheels
from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================



    def car_startup(self):
        distance = self.car.distance_detector.get_distance()
        while(True):
                self.car.accelerator.go_forward(50)
                distance = self.car.distance_detector.get_distance()

                if(distance <= 30 and distance != -1) :
                    # 가이드 라인 만날 때까지 우회전 전진
                    self.car.steering.turn_left(90 - 35)
                    self.car.accelerator.go_forward(50)


                    while(self.car.line_detector.is_in_line() == False):
                        pass

                    while(self.car.line_detector.is_in_line() == True):

                        if l == [0, 0, 0, 0, 1]:
                            self.car.steering.turn_right(90 + 35)
                            self.car.accelerator.go_forward(50)
                        elif l == [0, 0, 0, 1, 1]:
                            self.car.steering.turn_right(90 + 30)
                            self.car.accelerator.go_forward(50)
                        elif l == [0, 0, 0, 1, 0]:
                            self.car.steering.turn_right(90 + 10)
                            self.car.accelerator.go_forward(50)
                        elif l == [0, 0, 1, 1, 0]:
                            self.car.steering.turn_right(90 + 5)
                            self.car.accelerator.go_forward(50)
                        elif l == [0, 1, 1, 0, 0]:
                            self.car.steering.turn_left(90 - 5)
                            self.car.accelerator.go_forward(50)
                        elif l == [0, 1, 0, 0, 0]:
                            self.car.steering.turn_left(90 - 10)
                            self.car.accelerator.go_forward(50)
                        elif l == [1, 1, 0, 0, 0]:
                            self.car.steering.turn_left(90 - 30)
                            self.car.accelerator.go_forward(50)
                        elif l == [1, 0, 0, 0, 0]:
                            self.car.steering.turn_left(90 - 35)
                            self.car.accelerator.go_forward(50)
                        else:
                            self.car.accelerator.go_forward(50)


                    # 가이드 라인과 평팽하도록 좌회전 전진
                    self.car.steering.turn_right(90 + 35)
                    self.car.accelerator.go_forward(50)

                    while (self.car.line_detector.is_in_line() == False):
                        pass


                if (self.car.line_detector.is_in_line() == True):

                    l = self.car.line_detector.read_digital()
                    distance = self.car.distance_detector.get_distance()


                    # 라인트래싱
                    if l == [0, 0, 0, 0, 1]:
                        self.car.steering.turn_right(90 + 35)
                        self.car.accelerator.go_forward(50)
                    elif l == [0, 0, 0, 1, 1]:
                        self.car.steering.turn_right(90 + 30)
                        self.car.accelerator.go_forward(50)
                    elif l == [0, 0, 0, 1, 0]:
                        self.car.steering.turn_right(90 + 10)
                        self.car.accelerator.go_forward(50)
                    elif l == [0, 0, 1, 1, 0]:
                        self.car.steering.turn_right(90 + 5)
                        self.car.accelerator.go_forward(50)
                    elif l == [0, 1, 1, 0, 0]:
                        self.car.steering.turn_left(90 - 5)
                        self.car.accelerator.go_forward(50)
                    elif l == [0, 1, 0, 0, 0]:
                        self.car.steering.turn_left(90 - 10)
                        self.car.accelerator.go_forward(50)
                    elif l == [1, 1, 0, 0, 0]:
                        self.car.steering.turn_left(90 - 30)
                        self.car.accelerator.go_forward(50)
                    elif l == [1, 0, 0, 0, 0]:
                        self.car.steering.turn_left(90 - 35)
                        self.car.accelerator.go_forward(50)
                    else:
                        self.car.accelerator.go_forward(50)

                else:
                        # 우회전 후진
                    self.car.steering.turn_right(90 + 35)
                    self.car.accelerator.go_backward(100)
                    time.sleep(0.3)    # 좌회전 전진
                    self.car.steering.turn_left(90 - 35)
                    self.car.accelerator.go_forward(100)
                        # 전진
                    self.car.accelerator.go_forward(100)



            else:
                # 정지
                self.car.accelerator.stop()
                time.sleep(0.01)



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()

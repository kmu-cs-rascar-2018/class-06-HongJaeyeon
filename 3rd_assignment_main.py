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
        num = 0
        
        while (True):
            distance = self.car.distance_detector.get_distance()
            l = self.car.line_detector.read_digital()
            self.car.accelerator.go_forward(50)

            if (distance == -1):
                continue

            elif (distance <= 30):
                num += 1
                # 가이드 라인 만날 때까지 좌회전 전진
                self.car.steering.turn_left(90 - 35)
                self.car.accelerator.go_forward(50)
                #가이드 라인을 만나면 우회전 전진
                time.sleep(1)
                
                while True:
                    if self.car.line_detector.is_in_line() == True:
                        break
                    else:
                        continue
                self.car.accelerator.go_backward(50)
                time.sleep(0.4)
                self.car.steering.turn_right(90 + 35)
                self.car.accelerator.go_forward(40)
                time.sleep(2)
                
                while True:
                    if self.car.line_detector.is_in_line() == True:
                        break
                    else:
                        continue
                
            elif l == [0, 0, 0, 0, 1]:
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
            elif l == [0, 0, 0, 0, 0]:
                # 우회전 후진
                self.car.steering.turn_right(90 + 35)
                self.car.accelerator.go_backward(35)
                time.sleep(0.5)
                # 좌회전 전진
                self.car.steering.turn_left(90 - 35)
                self.car.accelerator.go_forward(30)
                time.sleep(0.45)
                # 전진
                self.car.accelerator.go_forward(50)
            elif l == [1, 1, 1, 1, 1]:
                if num == 4:
                    self.car.accelerator.stop()
                    time.sleep(3)
                    break
        
        
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        myCar.drive_parking()

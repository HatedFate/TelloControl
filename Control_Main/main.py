from projects import KeyPress as Kp
from djitellopy import Tello

drone = Tello()
drone.connect()


def activate():
    x = Drone()
    x.take_off()
    if Kp.pressed_keys("x"):
        x.status = False
        x.landing()


class Drone:

    status = True

    @staticmethod
    def take_off():
        drone.takeoff()

    @staticmethod
    def landing():
        drone.land()

    def __init__(self):
        self.up_down = 0
        self.front_back = 0
        self.left_right = 0
        self.turns = 0

    def commands(self):
        while self.status:
            self.movement()
            self.directions()

    def movement(self):
        drone.send_rc_control(self.left_right, self.front_back, self.up_down, self.turns)

    def directions(self):
        speed = 10
        if Kp.pressed_keys("a"):
            self.left_right = speed
        elif Kp.pressed_keys("d"):
            self.left_right = -speed
        if Kp.pressed_keys("w"):
            self.front_back = speed
        elif Kp.pressed_keys("s"):
            self.front_back = -speed


if __name__ == '__main__':
    activate()
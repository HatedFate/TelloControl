from projects import KeyPress as Kp
from djitellopy import Tello
from time import sleep

drone = Tello()
drone.connect()


def activate():
    x = Drone()
    x.commands()


class Drone:

    @staticmethod
    def take_off():
        drone.takeoff()

    @staticmethod
    def landing():
        drone.land()
        drone.end()

    @staticmethod
    def camera():
        drone.get_video_capture()

    def __init__(self):
        self.up_down = 0
        self.front_back = 0
        self.left_right = 0
        self.turns = 0
        self.status = True

    def commands(self):
        self.take_off()
        self.camera()
        while self.status:
            self.movement()
            self.directions()
            sleep(0.05)
            if Kp.pressed_keys("x"):
                self.status = False
                self.landing()

    def movement(self):
        drone.send_rc_control(self.left_right, self.front_back, self.up_down, self.turns)

    def directions(self):
        speed = 50
        if Kp.pressed_keys("a"):
            self.left_right = -speed
        elif Kp.pressed_keys("d"):
            self.left_right = speed
        if Kp.pressed_keys("w"):
            self.front_back = speed
        elif Kp.pressed_keys("s"):
            self.front_back = -speed
        if Kp.pressed_keys("q"):
            self.up_down = speed
        elif Kp.pressed_keys("e"):
            self.up_down = -speed


if __name__ == '__main__':
    activate()

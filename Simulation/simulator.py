from Control.PID_controller import PID
from Control.KeyControl import key_controller
import dronekit_sitl
import dronekit
import time

vehicle = dronekit.connect("udp:127.0.0.1:14551")  # Connect to Mission Planner simulator through UDP
gnd_speed = 5  # m/s


def arming(alt=10):
    while not vehicle.is_armable:
        print("Arming")
        time.sleep(1)

    vehicle.mode = dronekit.VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    vehicle.simple_takeoff(alt)





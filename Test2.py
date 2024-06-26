#!/usr/bin/env python3

from rover_api.discover_rover import Rover
from rover_api.discover_camera import Camera
from rover_api.discover_utils import finish_experiment

rover = Rover()
cam = Camera()


for i in range(4):
    rover.move_forward(0.2, 3)
    cam.get_jpg()
    rover.turn_right(15, 6) 

finish_experiment()

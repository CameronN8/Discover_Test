#!usr/bin/env python3

from rover_api.discover_rover import Rover
from rover_api.discover_utils import finish_experiment

rover = Rover()

rover.move_forward(0.2, 1)

#finish_experiment()

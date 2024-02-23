
'''
    Hello World Python Test
    
    File: main.py
    Author: Aidin Lehrman
    Version: 1-22-2024 15:25:55
'''

from pitop.robotics.blockpi_rover import BlockPiRover
from time import sleep
import math

def main():

    robot = BlockPiRover(left_motor="M0", right_motor="M3")

    TURN_CONSTANT: float = 0.395

    theta_radians: float = 0.5 * math.pi # 180 degrees
    speed: float = 0.25 # Unit-less: Gets units from 'SPEED_CONSTANT_METERS_PER_SECOND'

    # Calculates time to turn to turn 'theta_radians' with a turn radius of zero.
    time_seconds: float = (TURN_CONSTANT) * (theta_radians) / (2.0 * speed)

    for _ in range(10 * 4):
        robot.left(speed_factor = speed, turn_radius = 0.0)
        sleep(time_seconds)
        robot.stop()
        sleep(1)

    '''
    for _ in range(8):
        robot.forward(speed_factor = 1)
        sleep(2)

        robot.left(speed_factor = 1, turn_radius = 1 / 2)
        sleep((1 / 4) * math.pi)

    robot.stop()
    '''

if __name__ == '__main__':
    main()

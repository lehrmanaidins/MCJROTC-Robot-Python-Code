
'''
    Hello World Python Test
    
    File: main.py
    Author: Aidin Lehrman
    Version: 1-22-2024 15:25:55
'''

from pitop.processing.algorithms import process_frame_for_line
from pitop.camera import Camera
from pitop.camera.core.capture_actions import StoreFrame
from pitop.robotics.blockpi_rover import BlockPiRover
from time import sleep
import math

def main():

    robot = BlockPiRover(left_motor="M0", right_motor="M3")

    TURN_CONSTANT: float = 0.395

    theta_radians: float = 2 * math.pi # 180 degrees
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

def process_image(frame):
    processed_data = process_frame_for_line(frame)
    processed_frame = processed_data["robot_view"]
    return processed_frame

def capture_image():

    # process_frame_for_line(frame, image_format="PIL", process_image_width=320)
    camera = Camera()

    camera.start_handling_frames(
        callback_on_frame = process_image,
        frame_interval=1,
    )
    camera.start_video_capture()

    sleep(5)
    # print(f'Is Recording: {camera.is_recording()}')
    sleep(5)

    camera.stop_handling_frames()
    camera.stop_video_capture()
    # camera.capture_image(output_file_name="image_capture.png")

if __name__ == '__main__':
    capture_image()

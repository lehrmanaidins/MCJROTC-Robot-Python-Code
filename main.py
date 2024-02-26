
'''
    Main Python File
    
    File: main.py
    Author: Aidin Lehrman
    Version: 2-26-2024 10:06
'''

from pitop.processing.algorithms import process_frame_for_line
from pitop.camera import Camera
from pitop.robotics.blockpi_rover import BlockPiRover
from time import sleep
import math

def drive():
    # robot = BlockPiRover(left_motor="M0", right_motor="M3")
    robot = DriveController(left_motor_port="M0", right_motor_port="M3")

    robot.rotate(360, 5.0)
    for _ in range(4):
        robot.forward(1.0)
        sleep(1.0)
        robot.rotate(180, 2.5)

    robot.stop()

def process_image(frame):
    processed_data = process_frame_for_line(frame)
    processed_frame = processed_data["robot_view"]
    return processed_frame

def capture_video():

    # process_frame_for_line(frame, image_format="PIL", process_image_width=320)
    camera = Camera()

    camera.start_video_capture() # I think this has to be called before 'start_handling_frame' to process images properly
    camera.start_handling_frames( # Should outline blue line on every frame
        callback_on_frame = process_image,
        frame_interval = 1, # Has to be 1 to process image every frame
    )
    
    sleep(5.0) # Record for 5.0 seconds
    # print(f'Is Recording: {camera.is_recording()}')

    camera.stop_handling_frames()
    camera.stop_video_capture()
    # camera.capture_image(output_file_name="image_capture.png")

if __name__ == '__main__':
    capture_video()

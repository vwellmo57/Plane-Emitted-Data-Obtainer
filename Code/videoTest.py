import time
import picamera
import RPi.GPIO as GPIO
from time import sleep

camera = picamera.PiCamera()    # Setting up the camera
   
camera.start_recording('video2.h264') # Video will be saved at desktop

sleep(3)
camera.stop_recording()

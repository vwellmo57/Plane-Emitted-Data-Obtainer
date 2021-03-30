import time
import picamera
import RPi.GPIO as GPIO
from time import sleep

print("Start")
camera = picamera.PiCamera()    # Setting up the camera
camera.start_preview()      # You will see a preview window while recording
camera.start_recording('video2.mp4') # Video will be saved at desktop


sleep(3)
camera.stop_recording()
camera.stop_preview() 
print("Stop")

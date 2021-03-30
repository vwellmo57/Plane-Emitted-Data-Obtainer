import random
import time
import picamera
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)



def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)

def beginRecording():
    camera = picamera.PiCamera()    # Setting up the camera
    camera.start_recording(fileName() +'.h264') # Video will be saved at desktop
    

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)

def getAcceleration():
    return random.randint(1, 10000)

def fileName():
    name=time.asctime()
    return name


#file1 = open(r"D:\Text\accelerationinfo.txt","a+")
#file1.write(fileName()+"\n")
#for x in range(6):
#    z=str(getAcceleration())
#    file1.write("Acceleration: "+z + "\n")
    
#file1.close()
beginRecording()
sleep(3)
setAngle(35)
sleep(10)#right here buddy boy
camera.stop_recording()
pwm.stop()
GPIO.cleanup()

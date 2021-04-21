from flask import Flask, render_template, request
from time import sleep
import RPi.GPIO as GPIO
import random
import time
import picamera
import Adafruit_LSM303

camera = picamera.PiCamera()    # Setting up the camera
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)
acceleration = Adafruit_LSM303.LSM303()


app = Flask(__name__)
def beginRecording():
    camera.start_recording(fileName() +'.h264') # Video will be saved at desktop
    

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)

def getAcceleration():
   accel, mag = acceleration.read()
   accel_x, accel_y, accel_z = accel
   mag_x, mag_y, mag_z = mag
   return accel_x, accel_y, accel_z
    #return random.randint(1, 10000)

def fileName():
    name=time.asctime()
    return name




@app.route("/", methods=["GET","POST"])
def index():
	print(request.method)
    if request.method == 'POST':
        if request.form.get('button1') == 'button1':
   	        beginRecording()
            sleep(3)
            setAngle(35)
            file1 = open(r"accelerationinfo.txt","a+")
            file1.write(fileName()+"\n")
            for x in range(300):
                accelx,accely,accelz = getAcceleration()
                accelx = str(accelx)
                accely = str(accely)
                accelz = str(accelz)
                file1.write("X Axis: " + accelx + "  Y Axis: " + accely + "  Z Axis: " + accelz + "\n")
                sleep(.033333333333333)
                file1.write("\n")
                camera.stop_recording()
                pwm.stop()
                GPIO.cleanup()
      
        else:
            return render_template("index.html")

    elif request.method == 'GET':
         
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)

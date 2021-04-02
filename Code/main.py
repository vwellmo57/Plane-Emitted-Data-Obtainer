from flask import Flask, render_template, request
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)


app = Flask(__name__)
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)


@app.route("/", methods=["GET","POST"])
def index():
    print(request.method)
        if request.method == 'POST':
            if request.form.get('button1') == 'button1':
        SetAngle(0)
        sleep(1) 
        SetAngle(90)
        sleep(1) 
        SetAngle(0)       
            else:
                
                return render_template("index.html")

        elif request.method == 'GET':
           
            print("No Post Back Call")
        return render_template("index.html")


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)

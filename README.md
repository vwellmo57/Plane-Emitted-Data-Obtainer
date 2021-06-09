# Plane-Emitted-Data-Obtainer

## Building the Capsule
### Where We Compromised 
The design requirements for the capsule have been discussed in planning. That being said the actual version did not meet all of the requirements, namely size (which is not a big deal, it came in at 170g, under the goal of 200g) and the ability to be launched without a plane. The main reason for this was the friction created by the chute. Going in we did not expect there to be nearly as much friction between the top and the chute. The compromise was to just have the top remain on the plane after release. This was a compromise in that it did not allow the device to have as wide of a useful range and the plane's flight was very slightly negatively affected. 
### Construction
We wanted to have a slick design that screwed together, this was achieved by having the cap and the housing screw together along with a number of brass inserts. 

![Pic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkFgiztrQD9aHtxnAYWTAgmKN11DEYtGIxYA&usqp=CAU)

Inserts are installed by modeling a hole in your part and using heat (soldering iron) to install the insert which acts as a nut. These worked perfectly for our us and allowed everything to be screwed in (camera, accelerometer, servo), the Pi and power components were left without mounting as it would have been difficult to screw them in and they don't need to be mounted to serve their purpose. The images below show how we used threaded components:

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/850582074015875113/unknown.png)

A piece of acrylic was used to protect the lens and because it looks cool. The top and cap are held together with a shelf that registers them and a rubber band with string on the end that attaches to a servo arm and a fixed mount. The string slides into the casing and the contraption is released. 

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/850448115231883264/unknown.png)

Lastly, the parts were printed in PLA on Vann's 3-D printer. Truth be told, ABS would have been better but because of the massive amount of tolerancing work that had to be done with the threads, threaded insert holes, and servo holder, it was beneficial to use the fast turnaround time of a personal printer. ABS is better as it is lighter and bends when its yield strength is exceeded as opposed to PLA which snaps (brittle). Although less than ideal, the capsule was dropped from a bridge 3 times, a plane 2 times, and thrown off a bridge without a parachute once, no parts broke and the only reprints were parts that did not fit, nothing broke. 

### What We Should Have Done Better (Capsule) 
The capsule fundamentally worked, a larger cap would have solved the chute friction issues but the compressed timeline did not give us time to fix what would have required a massive redesign. The only other concern with the capsule is the direct mechanical connection between sensitive electronics and the capsule. The chute has a shock cord that distributes the deceleration over time but if dropped the capsule could send shock waves into electronics. This could potentially be solved by rubber washers or an o-ring although this is speculation. Other changes would be a small shelf or tube so that the rod doesn't fall out when retracted and a rotation of the slot that holds to a rubber band. In its current form, it has the band come off at an unideal angle. 

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/850585454164049950/unknown.png)

## The Electronics
The electronics were comparatively simple. We used a Raspberry Pi Zero, Power Boost 500c, a 3.7V 350mAh LiPo, camera, 180-degree servo, and an LSM303DLHC. The LiPo plugged into the power boost which powered the Pi. Wiring was fairly straightforward, pins were soldered onto the accelerometer. The largest challenge for electronics was getting everything to fit, ultimately it worked out, the use of silicon wires helped as they are far more flexible. The pic below shows the wiring diagram:

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/851148484412702740/unknown.png)

## Coding
### The Goals
* Friendliness - Easy to use
* Efficiency - Runs and smoothly and quickly as possible
* Flexibility - Can be used in different scenarios that may occur

### Camera
```python
camera = picamera.PiCamera()    # Setting up the camera
def beginRecording(): 
    camera.start_recording(fileName() +'.h264') # Video saves to same directory as code
```
### Release
```python
def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)
```

### Acceleration
```python
acceleration = Adafruit_LSM303.LSM303() # Assigning accelerometer
def getAcceleration():
   accel = acceleration.read() # Reads current acceleration data
   accel_x, accel_y, accel_z = accel # Assigns to different planes
   return accel_x, accel_y, accel_z # Returns seperate acceleration info
```
Example of Saved Accleration Information 
```
Mon Apr 26 14:57:23 2021
X Axis: 9  Y Axis: -982  Z Axis: -251

X Axis: 11  Y Axis: -982  Z Axis: -249

X Axis: 11  Y Axis: -982  Z Axis: -249

X Axis: 8  Y Axis: -981  Z Axis: -245

X Axis: 8  Y Axis: -981  Z Axis: -245
```

### Filename
```python
def fileName():
    return time.asctime() # Simply returns time and date info
```

### Body
```python
		if request.form.get('button1') == 'button1': 
			beginRecording() # Starts recording
			sleep(3) # Gives pilot 3 seconds to find perfect position
			setAngle(35) # Drops the capsule
			file1 = open(r"accelerationinfo.txt","a+") # Prepares to save acceleration data
			file1.write(fileName()+"\n") # Writes the date and time into a text document
			for x in range(300): # 10 seconds
				accelx,accely,accelz = getAcceleration() # Gathers acceleration info and declares them as strings
				accelx = str(accelx)
				accely = str(accely)
				accelz = str(accelz)
				file1.write("X Axis: " + accelx + "  Y Axis: " + accely + "  Z Axis: " + accelz + "\n") # Saves and formats acceleration info
				sleep(.033333333333333)
				file1.write("\n") # New line
			camera.stop_recording() # End recording
			pwm.stop() # Cleans up
			GPIO.cleanup()
```
### HTML
```htm
<button type="submit" name="button1" class="button button-primary" value="button1">Drop</button> <!-- Declares button and allows it to communicate with python code-->
```
### Challenges
Since we were both working at our homes, we had some challenges getting all the parts of the project to work with each other. Early in the year Vann's Raspberry Pi stopped working so he was using Philip's in the capsule. This meant that Philip had to code everything in VS Code and send the code to Vann without testing it. Luckily he was able to find and use helpful resources online which meant he didn't have to test his code as frequently. The most difficult part of the coding process was coding the accelerometer and the camera since there was not much documentation available online on how to record using the camera or how to collect acceleration data and output it into a text document. To bypass these issues Philip and Vann screenshared over Zoom, allowing Philip to see exactly what was going wrong with his code and how to fix it. 
### How We achieved Our Goals
#### Friendliness
The website's UI is very clean and responsive on mobile. We could easily connect to the Pi and give it commands without worrying about anything else. 

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/851180925467099196/unknown.png)

#### Efficiency 
All of the code was broken into functions. Not only super easy for us to edit the code on a phone, but it minimized file sizes and allowed us to focus on the main body of code which is where we would edit delays and timings. 
#### Flexibility
Since we had three different buttons on the website, we could drop the capsule and manually deploy the parachute, OR we could run them both at the click of one button. We generally opted to just use one button, but in case that anything failed we were able to re-run the steps that did not work. 

## The Results

After dropping the Pi, the acceleration data and footage from the capsule's camera corrupted. The capsule's code and mechanics worked flawlessly, but due to a crash that rendered the plane completely broken, we were unable to have any further attempts. We decided to drop the Pi from a tall bridge to try to mimic the results. 

## Deployment

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/849646585380995112/unknown.png)

Our Pi was controlled by this website, the three buttons on the screen allowed us to control every aspect of our drop. Selecting the "Drop and Deploy" button would release the capsule from the plane and deploy its parachute.

Compilation of 2 plane drops and the bridge drop: https://www.youtube.com/watch?v=wqw0opE7P7w

Plane drop: https://github.com/vwellmo57/Plane-Emitted-Data-Obtainer/blob/main/Media/ShakeAndBake2000.mp4 

Bridge drop: https://github.com/vwellmo57/Plane-Emitted-Data-Obtainer/blob/main/Media/Mon_May_31_20_30_12_2021_(1).mp4 


## Acceleration Data

You can view all of the acceleration data here: https://github.com/vwellmo57/Plane-Emitted-Data-Obtainer/blob/main/Media/accelerationinfo.txt

Highlights:
* Focus on the Z Axis
* Line 23: Capsule is dropped
* Line ~93: Parachute is deployed
* Line 145: Landing

![Pic](https://media.discordapp.net/attachments/356809004141248512/849662701931986974/unknown.png)

## Conclusion

Overall the project was a success. Even though some goals were not accomplished the central goal to drop a thing from a plane and collect data was a success (up until the data corrupted). The capsule worked excellently, as did the code. The only consistent failure was the electronics failing in some way. Another challenge was not being able to work together but by dividing the work efficiently everything got finished. 

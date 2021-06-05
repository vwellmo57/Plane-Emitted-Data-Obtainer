# Plane-Emitted-Data-Obtainer

## The Results

After dropping the Pi, the acceleration data and footage from the capsule's camera corrupted. The capsule's code and mechanics worked flawlessly, but due to a crash that rendered the plane completely broken we were unable to have any further attempts. We decided to drop the Pi from a tall bridge to try to mimic the results. 

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

## Building the Capsule
### Where We Compromised 
The design requirements for the capsule have been discussed in planning. That being said the actual version did not meet all of the requirements, namely size (which is not a big deal, it came in at 170g, under the goal of 200g) and it is able to be launched without a plane (such as off a catapult). The main reason for this was the friction created by the chute. Going in we did not expect there to be nearly as much friction between the top and the chute. The compromise was to just have the top remain on the plane after release. This was a compromise in that it did not allow the device to have as wide of a useful range and the plane's flight was very slightly negatively affected. 
### Construction
We wanted to have a slick design that screwed together, this was achived by having the cap and the housing screw together anlong with a number of brass inserts. 

![Pic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkFgiztrQD9aHtxnAYWTAgmKN11DEYtGIxYA&usqp=CAU)

Insterts are installed by moideling a hole in your part and using heat (soldering iron) to install the insert which acts as a nut. These worked perfectly for our use case and allowed everything to be screwed in (camera, accelerometer, servo), the pi and power components were left without mounting as it would have been difficult to screw them in and they don't need to be mounted to serve their purpose. The images below show the how we used threaded components:

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/850582074015875113/unknown.png)

A piece of acrylic was used to protect the lens and because it looks cool. The top and cap are held together with a shelf that registers them and a rubber band with string on the end that attaches to a servo arm and fixed mount. The string slides into the casing and the contraption is released. 

![Pic](https://cdn.discordapp.com/attachments/356809004141248512/850448115231883264/unknown.png)

Lastly, the parts were printed in PLA on Vann's 3-D printer. Truth be told ABS would have been better but because of the massive amount of tolerancing work that had to be done with the threads, threaded insert holes, and servo holder, it was beneficial to use the fast turn around time of a personal printer. ABS is better as it is lighter and bends when its yield strength is exedded as opposed to PLA which snaps (brittle). 

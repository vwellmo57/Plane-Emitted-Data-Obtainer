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

# Planning

## What We Want To Have
  Our main goal going into this project is to drop something from a remote-controlled plane and for that thing to collect data possibly from the flight but definitely from the fall. The plane would be small with a wingspan of around a meter and the "thing" will have to be quite small as well, ideally under ~150 mm. 

## Easily Foreseeable Issues
  We can already identify lots of problems by involving a plane, mainly weight and aerodynamics. When we drop the "thing" we will lose lot's of the plane's mass, this will make the plane fly very different as it will have a much lower mass and will fly quicker. To compensate for this we need a very light "thing" that will not produce much lift while under the plane. 
  The other main issue is how will the "thing" survive? It will be falling from about 10 or more meters and with a 200-gram thing it would hit the ground at about 14 m/s, that is very fast and would almost certainly destroy a pi without adequate protection. To solve this we will use a parachute that will deploy either after released from the plane or at an operator-controlled time. 

## The Plan
### The Housing
The housing will hold all of the electronics such as the raspi, a camera, power, servo, accelerometer, and anything else we need. The camera will be positioned so it can take pictures or video of the ground while falling. It, the accelerometer, and the servo will need to be bolted so they can't move, the other components don't need to be bolted. 
### The Cap
The cap will screw onto the housing and serves to keep it safe if parachute deployment fails by isolating them from the outside. It also registers with the last component. 
### The Top
The top will be loosely fit onto the cap but able to fall off. It is held in place by a rubber band and servo arm and when released should fly off and release the chute. 
### Picture
![Pic](https://github.com/vwellmo57/Plane-Emitted-Data-Obtainer/blob/main/Planning/Media/whiteboardPlane.jpg)

## Division of Labor
### Philip
Philip will build the planes and CAD them. He will also write some of the code for the device (most likely the webpage).
### Vann
Vann will CAD and build the device as well as write some of the code. He will also wire control surfaces for the place. 


## Timeline
* March 1st - CAD for both the plane and the capsule
* March 25th - Prototype plane and capsule constructed
* April 15th - Completed a test drop with the capsule
* April 25th - Capsule completely done
* May 15th - Final Plane done
* May 30th - Successful plane drop

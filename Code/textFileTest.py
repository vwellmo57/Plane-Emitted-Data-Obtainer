import random
import time

def getAcceleration():
    return random.randint(1, 10000)

def fileName():
    name=time.asctime()
    return name


file1 = open(r"accelerationinfo.txt","a+")
file1.write(fileName()+"\n")
for x in range(6):
    z=str(getAcceleration())
    file1.write("Acceleration: "+z + "\n")
    
file1.close()

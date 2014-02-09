from piglow import PiGlow
from time import sleep
import math
piglow = PiGlow()

piglow.all(0)




def phase():
    for t in range(0,360):
        for colour in range(0,5):
            for arm in range(0,3):
                b1 = math.sin(math.radians(-t + arm * 30 +  colour * 360/5))

                brightness = max(0, min(int(-128 + 256 * b1),255))
                led = int((6*arm)+colour)+1
                #print(colour,arm,led,degrees,rad,brightness)
                piglow.led(led, brightness)
        sleep(0.1) 


def dazzle():
    for t1 in range(0,360,10):
        for t2 in range(0,360,10):
            for colour in range(0,6):
                for arm in range(0,3):
                    b1 = math.sin(math.radians(6 * math.sin(math.radians(t1)) * t2 * (colour+1)))

                    brightness = max(0, min(int(-128 + 256 * b1),255))
                    led = int((6*arm)+colour)+1
                    #print(colour,arm,led,degrees,rad,brightness)
                    piglow.led(led, brightness)
            sleep(0.05) 
def spin():
    for t1 in range(0,360,10):
        for t2 in range(0,360,10):
            for colour in range(0,6):
                for arm in range(0,3):
                    b1 = math.sin(math.radians(colour * (180/6) * math.sin(math.radians(t1)) + arm * (180/3) * math.cos(math.radians(t1)) + t2))

                    brightness = max(0, min(int(-128 + 256 * b1),255))
                    led = int((6*arm)+colour)+1
                    #print(colour,arm,led,degrees,rad,brightness)
                    piglow.led(led, brightness)
            sleep(0.05)
while True:
    spin()
    dazzle()
    phase()


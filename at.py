from piglow import PiGlow
from time import sleep
import math
piglow = PiGlow()


maxbright = 8
piglow.all(0)



def getLed(arm,colour):
    return int(6*arm+colour+1)
def getBright(factor):
    return max(0, min(int(-0.25 * maxbright + maxbright * factor),255))
def phase():
    for t in range(0,360):
        for colour in range(0,5):
            for arm in range(0,3):
                b1 = math.sin(math.radians(-t + arm * 30 +  colour * 360/5))
                piglow.led(getLed(arm,colour), getBright(b1))
        sleep(0.1) 


def dazzle():
    for t1 in range(0,360,10):
        for t2 in range(0,360,10):
            for colour in range(0,6):
                for arm in range(0,3):
                    b1 = math.sin(math.radians(t2 + arm * (90/3) * math.cos(math.radians(t1))  + colour * (360/6) * math.sin(math.radians(t1))))            
                    piglow.led(getLed(arm,colour), getBright(b1))
            sleep(0.05) 
def spin():
    for t1 in range(0,360,10):
        for t2 in range(0,360,10):
            for colour in range(0,6):
                for arm in range(0,3):
                    b1 = math.sin(math.radians(t2 + arm * (360/3) * math.cos(math.radians(t1)) + colour * (90/6) * math.sin(math.radians(t1))))
                    piglow.led(getLed(arm,colour), getBright(b1))

            sleep(0.05)

def attention():
    for direction in (-1,+1):
        for t1 in range(-180,180,10):
            for colour in range(0,6):
                for arm in range(0,3):
                    b1 = math.sin(math.radians(direction * t1 + arm * 90/3 + colour * 90/6))
                    piglow.led(getLed(arm,colour), getBright(b1))

            sleep(0.05)
while True:
    #spin()
    #dazzle()
    #phase()
    attention()

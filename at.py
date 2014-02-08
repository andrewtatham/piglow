from piglow import PiGlow
from time import sleep
import math
piglow = PiGlow()

piglow.all(0)


while True:
    for t in range(0,360):
        for colour in range(0,5):
            for arm in range(0,3):
                b1 = math.sin(math.radians(-t + arm * 30 +  colour * 360/5))

                brightness = max(0, min(int(-128 + 256 * b1),255))
                led = int((6*arm)+colour)+1
                #print(colour,arm,led,degrees,rad,brightness)
                piglow.led(led, brightness)
        sleep(0.1) 









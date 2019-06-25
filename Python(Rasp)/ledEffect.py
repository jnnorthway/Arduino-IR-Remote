import pigpio
import time
pi = pigpio.pi()

pin = [17,22,27]
eff = 0
boolLoop = True
li = [[80,0,80 , 0,255,255 , 80,0,80],[255,0,0 , 0,255,0 , 0,0,255 , 255,255,0 , 80,0,80 , 0,255,255]]
i = 0
r = li[eff][0]
g = li[eff][1]
b = li[eff][2]
while boolLoop:
    red = li[eff][i%len(li[eff])]
    green = li[eff][(i+1)%len(li[eff])]
    blue = li[eff][(i+2)%len(li[eff])]
    i+=3
    while ( r != red or g != green or b != blue ):
        if ( r < red ):
            r += 1
        if ( r > red ):
            r -= 1

        if ( g < green ):
            g += 1
        if ( g > green ):
            g -= 1

        if ( b < blue ):
            b += 1
        if ( b > blue ):
            b -= 1

        pi.set_PWM_dutycycle(pin[0], r)
        pi.set_PWM_dutycycle(pin[1], g)
        pi.set_PWM_dutycycle(pin[2], b)
        time.sleep(0.01)

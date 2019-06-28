import pigpio
import time
import sys
pi = pigpio.pi()

li=[[],[],[],[],[],[]]
pin = [17,22,27]
f=open("/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/Effects.txt", "r")
if f.mode == 'r':
    f1 = f.readlines()
    count = 0
    for x in f1:
        j=0
        for element in x:
            if element != ',':
                li[count][j] += element
            else:
                j+=1
        count += 1

#li = [[80,0,80 , 0,255,255 , 80,0,80],[255,0,0 , 0,255,0 , 0,0,255 , 255,255,0 , 80,0,80 , 0,255,255]]

def runEffect(eff):
    i = 0
    r = li[eff][0]
    g = li[eff][1]
    b = li[eff][2]
    while True:
        red = int(li[eff][i%len(li[eff])])
        green = int(li[eff][(i+1)%len(li[eff])])
        blue = int(li[eff][(i+2)%len(li[eff])])
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

runEffect(int(sys.argv[1]))

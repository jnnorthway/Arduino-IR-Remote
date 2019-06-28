#!/usr/bin/env python3
from tkinter import *
from tkinter.colorchooser import *
import sys
import pigpio
import subprocess
import threading
import time

pi = pigpio.pi()

#global variables
LedOn = False
effectOn = False
sizeX = 800
sizeY = 480
LEDRED=0
LEDGREEN=0
LEDBLUE=0
pin = [17,22,27]
effectChosen = 0



def exit():
    pi.set_PWM_dutycycle(pin[0], 0)
    pi.set_PWM_dutycycle(pin[1], 0)
    pi.set_PWM_dutycycle(pin[2], 0)
    sys.exit()

#forget object placement
def forget(list):
    for i in list:
        i.place_forget()

#place objects into frame
def place(list1, list2):
    j = 0
    if((len(list2) / len(list1)) == 2):
        for i in list1:
            i.place(x=list2[j], y=list2[j+1])
            j+=2
    else:
        for i in list1:
            i.place(x=list2[j], y=list2[j+1], width=list2[j+2])
            j+=3

#translate rgb colour to hex
def translate(rgb):
    return "#%02x%02x%02x" % rgb

#samsung menu
def Samsung():
    forget(menuList)
    place(samsungList, samsungListCoord)

#led menu
def Led():
    forget(menuList)
    forget(coloursList)
    forget(effectsList)
    place(ledList, ledListCoord)

#colour pick menu
def Colours():
    forget(ledList)
    place(coloursList, coloursListCoord)

#update frame to show colour
def updateColour(s):
    colourFrame.configure(bg= translate((colourR.get(), colourG.get(), colourB.get())))

def selectColour():
    if LedOn:
        subprocess.call(["sudo", "pkill", "-f", "ledEffect.py"])
        global effectOn
        effectOn = False
        global LEDRED
        LEDRED = colourR.get()
        pi.set_PWM_dutycycle(pin[0], LEDRED)
        global LEDGREEN
        LEDGREEN = colourG.get()
        pi.set_PWM_dutycycle(pin[1], LEDGREEN)
        global LEDBLUE
        LEDBLUE = colourB.get()
        pi.set_PWM_dutycycle(pin[2], LEDBLUE)

def LedPower():
    global LedOn
    if LedOn:
        subprocess.call(["sudo", "pkill", "-f", "ledEffect.py"])
        pi.set_PWM_dutycycle(pin[0], 0)
        pi.set_PWM_dutycycle(pin[1], 0)
        pi.set_PWM_dutycycle(pin[2], 0)
        LedOn = False
    else:
        LedOn = True
        selectColour()

def sleep():
    pass

#effects menu
def Effects():
    forget(ledList)
    place(effectsList, effectsListCoord)

def callEffect():
    subprocess.call(["sudo", "python3", "/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/ledEffect.py", str(effectChosen)])

def selectEffect():
    if LedOn:
        subprocess.call(["sudo", "pkill", "-f", "ledEffect.py"])
        effectOn = True
        t1 = threading.Thread(target=callEffect)
        t1.start()

def runEffect(li, eff):
    r = li[eff][0]
    g = li[eff][1]
    b = li[eff][2]
    i = 3
    global effectChosen
    effectChosen = eff
    while i < len(li[eff]):
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

            effectColourFrame.after(5,sleep())
            effectColourFrame.configure(bg= translate((r,g,b)))
            root.update()

def pBtn():
    PowerB.place(x=50, y=380)

#main menu
def menu():
    forget(samsungList)
    forget(ledList)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    place(menuList, menuListCoord)

def tick():
    time1.set(time.strftime("%H:%M:%S"))
    clock.after(500, tick)

root = Tk()
root.geometry(str(sizeX) + "x" + str(sizeY))
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.config(cursor="none")

title = Frame(root).place(width = sizeX, height = 150, x = 0, y = 0)
version = Frame(root).place(width = sizeX, height = sizeY, x = 0, y = 0)
time = Frame(root).place(width = sizeX, height = sizeY, x = 0, y = 0)
main = Frame(root)

main.place(width = sizeX, height = sizeY, x = 0, y = 0)
bg1 = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/bg1.png")
background_label = Label(main, image=bg1)
pwr = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/pwrBtn.png")
pwr2 = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/pwr2.png")
volUp = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/volUp.png")
volDown = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/volDown.png")
volMute = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/volMute.png")
plus = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/plus.png")
minus = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/minus.png")
rgbImg = PhotoImage(file="/home/pi/Desktop/github/Desktop-Remote/Python(Rasp)/images/rgbImg2.png")
rgbPic = Label(root, image=rgbImg)

#Labels
time1 = StringVar()
title = Label(title, text="Desktop Remote", bg="#ff0c85", fg="#ffc9e3", font=("Arial", 44))
version = Label(version, text="v2.0", bg="#ff0c85", fg="#ffc9e3", font=("Arial", 20))
clock = Label(main, textvariable=time1, bg="#ff0c85", fg="#ffc9e3", font=("Arial", 20))

#----Menu------------------------------------------------------------------------------------------------------------
LedB = Button(main, text="LED", bg="white", fg="black", font=("Arial", 20), command=Led)
SamsungB = Button(main, text="Samsung", bg="white", fg="black", font=("Arial", 20), command=Samsung)

PowerB = Button(image=pwr, command=exit)
PowerB["bg"] = "black"
PowerB["border"] = "0"

menuList = [title, version, LedB, SamsungB, clock]
menuListCoord = [175,0,450 , 720,440,80 , 100,240,200 , 500,240,200 , 720,0,80]

#----Universal------------------------------------------------------------------------------------------------------------
backBtn = Button(main, text="BACK", bg="black", fg="white", font=("Arial", 20), command=menu)
backLedBtn = Button(main, text="BACK", bg="black", fg="white", font=("Arial", 20), command=Led)

#----Samsung------------------------------------------------------------------------------------------------------------
SamPwrB = Button(image=pwr2)
SamSource = Button(main, text="Source", bg="white", fg="black", font=("Arial", 20))
SamVolumeUp = Button(image=volUp)
SamVolumeDown = Button(image=volDown)
SamVolumeMute = Button(image=volMute)
SamPlus = Button(image=plus)
SamMinus = Button(image=minus)

samsungList = [SamPwrB, SamSource, SamVolumeUp, SamVolumeDown, SamVolumeMute, SamPlus, SamMinus, backBtn]
samsungListCoord = [50,120 , 480,75 , 240,60, 240,340 , 240,200 , 490,200 , 490,340 , 50,50]

#----LED------------------------------------------------------------------------------------------------------------
LedPwrB = Button(image=pwr2, command=LedPower)
LedColours = Button(main, text="Colours", bg="white", fg="black", font=("Arial", 20), command=Colours)
LedEffects = Button(main, text="Effects", bg="white", fg="black", font=("Arial", 20), command=Effects)

ledList = [LedPwrB, rgbPic, LedColours, LedEffects, backBtn]
ledListCoord = [50,120 , 200,75 , 275,350 , 550,350 , 50,50]

#----Colours------------------------------------------------------------------------------------------------------------
colourR = Scale(main, bg="#f24f43", fg="white", from_=255, to=0, showvalue=0, font=("Arial", 12), length=200, width=50, command=updateColour)
colourR.set(255)
colourG = Scale(main, bg="#47ce35", fg="white", from_=255, to=0, showvalue=0, font=("Arial", 12), length=200, width=50, command=updateColour)
colourG.set(255)
colourB = Scale(main, bg="#3553ce", fg="white", from_=255, to=0, showvalue=0, font=("Arial", 12), length=200, width=50, command=updateColour)
colourB.set(255)
brightness = Scale(main, bg="black", fg="white", from_=1, to=256, showvalue=0, font=("Arial", 12), orient=HORIZONTAL, length=200, width=30)
brightness.set(255)
colourBlackFrame = Frame(root, width=110, height=110, bg="#52565e")
colourFrame = Frame(root, width=100, height=100, bg= translate((colourR.get(), colourG.get(), colourB.get())))
setColour = Button(main, text="Set Colour", bg="white", fg="black", font=("Arial", 20), command=selectColour)

coloursList = [LedPwrB, colourR , colourG , colourB, colourFrame, colourBlackFrame, setColour, backLedBtn]
coloursListCoord = [50,120 , 200,125 , 300,125 , 400,125 , 505,140 , 500,135 , 480,270 , 50,50]

#----Effects------------------------------------------------------------------------------------------------------------
effectColourBlackFrame = Frame(root, width=110, height=110, bg="#52565e")
effectColourFrame = Frame(root, width=100, height=100, bg="white")
clrEffectList = [
[255,0,255,0,255,255,255,0,255]
,[255,0,0 , 255,128,0 , 255,255,0 , 128,255,0 , 0,255,0 , 0,255,128 , 0,255,255 , 0,128,255 , 0,0,255 , 128,0,255 , 255,0,255 , 255,0,255 , 255,0,128 , 255,0,0]
,[255,0,255,0,0,0,255,0,255]
,[128,0,255,0,0,0,128,0,255]
,[0,255,255,0,0,0,0,255,255]
,[255,0,255,128,0,255,255,0,255]
]
Effect1 = Button(main, text="Effect1", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
Effect2 = Button(main, text="Effect2", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 1))
Effect3 = Button(main, text="Effect3", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 2))
Effect4 = Button(main, text="Effect4", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 3))
Effect5 = Button(main, text="Effect5", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 4))
Effect6 = Button(main, text="Effect6", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 5))
setEffect = Button(main, text="Set Effect", bg="white", fg="black", font=("Arial", 20), command=selectEffect)

effectsList = [LedPwrB, Effect1, Effect2, Effect3, Effect4, Effect5, Effect6, effectColourFrame, effectColourBlackFrame, setEffect, backLedBtn]
effectsListCoord = [50,120 , 200,150 , 350,150 , 500,150 , 200,250 , 350,250 , 500,250 , 650,130 , 645,125 , 630,250 , 50,50]

menu()
pBtn()
tick()
root.mainloop()

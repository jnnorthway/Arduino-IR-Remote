from tkinter import *
from tkinter.colorchooser import *
import sys

sizeX = 800
sizeY = 480
MAX_LIGHT = 256

def exit():
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
    colourFrame.configure(bg= translate((colourR.get()%MAX_LIGHT, colourG.get()%MAX_LIGHT, colourB.get()%MAX_LIGHT)))

def updateBrightness(s):
    global MAX_LIGHT
    MAX_LIGHT = brightness.get()
    updateColour(s)

def sleep():
    pass

#effects menu
def Effects():
    forget(ledList)
    place(effectsList, effectsListCoord)

def runEffect(li, eff):
    r = li[eff][0]
    g = li[eff][1]
    b = li[eff][2]
    global boolLoop
    boolLoop = True
    i = 3
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

root = Tk()
root.geometry(str(sizeX) + "x" + str(sizeY))
root.configure(bg="black")
title = Frame(root).place(width = sizeX, height = 150, x = 0, y = 0)
version = Frame(root).place(width = sizeX, height = sizeY, x = 0, y = 0)
main = Frame(root).place(width = sizeX, height = 650, x = 0, y = 200)
bg1 = PhotoImage(file="images/bg1.png")
background_label = Label(main, image=bg1)
pwr = PhotoImage(file="images\pwrBtn.png")
pwr2 = PhotoImage(file="images\pwr2.png")
volUp = PhotoImage(file="images\\volUp.png")
volDown = PhotoImage(file="images\\volDown.png")
volMute = PhotoImage(file="images\\volMute.png")
plus = PhotoImage(file="images\plus.png")
minus = PhotoImage(file="images\minus.png")
rgbImg = PhotoImage(file="images\\rgbImg2.png")
rgbPic = Label(root, image=rgbImg)

#Labels
title = Label(title, text="IR Controller", bg="#ff0c85", fg="#ffc9e3", font=("Arial", 44))
version = Label(version, text="v1.1", bg="#ff0c85", fg="#ffc9e3", font=("Arial", 20))

#----Menu------------------------------------------------------------------------------------------------------------
LedB = Button(main, text="LED", bg="white", fg="black", font=("Arial", 20), command=Led)
SamsungB = Button(main, text="Samsung", bg="white", fg="black", font=("Arial", 20), command=Samsung)

PowerB = Button(image=pwr, command=exit)
PowerB["bg"] = "black"
PowerB["border"] = "0"

menuList = [title, version, LedB, SamsungB]
menuListCoord = [175,0,450 , 720,440,80 , 100,240,200 , 500,240,200]

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
LedPwrB = Button(image=pwr2)
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
brightness = Scale(main, bg="black", fg="white", from_=1, to=256, showvalue=0, font=("Arial", 12), orient=HORIZONTAL, length=200, width=30, command=updateBrightness)
brightness.set(256)
colourBlackFrame = Frame(root, width=110, height=110, bg="#52565e")
colourFrame = Frame(root, width=100, height=100, bg= translate((colourR.get(), colourG.get(), colourB.get())))
setColour = Button(main, text="Set Colour", bg="white", fg="black", font=("Arial", 20))

coloursList = [LedPwrB, colourR , colourG , colourB, brightness, colourFrame, colourBlackFrame, setColour, backLedBtn]
coloursListCoord = [50,120 , 200,125 , 300,125 , 400,125 , 200,350 , 505,140 , 500,135 , 480,270 , 50,50]

#----Effects------------------------------------------------------------------------------------------------------------
effectColourBlackFrame = Frame(root, width=110, height=110, bg="#52565e")
effectColourFrame = Frame(root, width=100, height=100, bg="white")
clrEffectList = [[80,0,80 , 0,255,255 , 80,0,80],[255,0,0 , 0,255,0 , 0,0,255 , 255,255,0 , 80,0,80 , 0,255,255]]
Effect1 = Button(main, text="Effect1", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
Effect2 = Button(main, text="Effect2", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 1))
Effect3 = Button(main, text="Effect3", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
Effect4 = Button(main, text="Effect4", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
Effect5 = Button(main, text="Effect5", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
Effect6 = Button(main, text="Effect6", bg="white", fg="black", font=("Arial", 20), command=lambda: runEffect(clrEffectList, 0))
setEffect = Button(main, text="Set Effect", bg="white", fg="black", font=("Arial", 20))

effectsList = [LedPwrB, Effect1, Effect2, Effect3, Effect4, Effect5, Effect6, effectColourFrame, effectColourBlackFrame, setEffect, backLedBtn]
effectsListCoord = [50,120 , 180,150 , 330,150 , 480,150 , 180,250 , 330,250 , 480,250 , 630,130 , 625,125 , 610,250 , 50,50]

menu()
pBtn()

root.mainloop()

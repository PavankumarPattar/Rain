from tkinter import *
import random
from Rain import *
import time

window = Tk()

canvas=Canvas(window,width=500,height=400,background="black")
canvas.pack()

rain=[]
for i in range(200):
    rain.append(i)

y,y0=20,0
for i in range(200):
    x=random.randint(-20,500)
    y0=random.randint(1,100)
    yVel=random.randint(1,5)
    # (x,y,x0,y0)here x & x0 hase to b equal to move left or right
    # and y & y0 should be y+10 & y (ex: y=20 ,y0=10)
    rain[i]= Rain(canvas,x,y0+20,x,y0,0,yVel,"lightgreen")
    
while True:
    for i in range(200):
        rain[i].move()
    
    window.update()
    time.sleep(0.01)

window.mainloop()
import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(1000)
bgcolor("black")    

for i in range(5):
    write("My Lifeline    \n    MomDad", align="center", font=("Algerian", 24, "normal"))
    color("white")

for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    pencolor("red") 

goto(0,0)
done()

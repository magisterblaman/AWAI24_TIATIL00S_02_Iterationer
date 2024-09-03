from turtle import *

speed(1)

for i in range(8):
    pendown()
    forward(100)
    penup()
    right(180)
    forward(20)
    pendown()
    left(135)
    forward(20)
    penup()
    back(20)
    pendown()
    left(90)
    forward(20)
    back(20)
    right(45)
    penup()
    back(80)
    right(45)

done()
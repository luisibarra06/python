#thingy.py	lai
import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('#FFFFFF')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('#000000')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('#C6C60D')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('#2F3BDA')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('#A0080D')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Terry,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('#BA00FF')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)

import turtle
import math
bob = turtle.Turtle()

def polygon(t, length, n):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle (t,r):
    circunference = 2 * math.pi * r
    n = int(circunference / 3)+1
    length = circunference / n
    angle = 360.0 / n
    polygon(t, length, n)

circle(bob, 100)

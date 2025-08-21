import turtle
import math

bob = turtle.Turtle()

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.rt(step_angle)

def drawHeart(t):
    t.lt(90)
    arc(t,50,180)
    t.lt(180)
    arc(t, 50, 180)
    t.rt(30)
    t.fd(202)
    t.rt(120)
    t.fd(200)

drawHeart(bob)
bob.up()
bob.fd(20000)
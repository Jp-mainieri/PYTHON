#Flores
import math
import turtle
bob = turtle.Turtle()


def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
p = 20
angle = 420/p
r = 100 * p/10
for i in range(p):
    arc(bob,r,angle)
    bob.lt(180-angle)
    arc(bob, r, angle)
    bob.lt(180-angle)
    bob.lt(360/p)

#arc(bob,100,330)

import math
import turtle

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)  # FOWARD
        t.lt(angle)  # LEFT TURN
def arc(t,r,angle):
    """Desenha um arco de cirucunferência
     de raio r e angulo angle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t,n,step_length,step_angle)

def circle(t,r):
    arc(t,r,360)


circle(bob,100)
bob.fd(50)
arc(bob,100,180)




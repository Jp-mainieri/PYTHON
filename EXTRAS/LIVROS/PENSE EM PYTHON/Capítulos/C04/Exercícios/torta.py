import turtle

bob = turtle.Turtle()

def triangle(t,n,length):
    for i in range(3):
        line(t,length,180-((360/n)/2)/2)
def line(t,length,angle):
    t.fd(length)
    t.lt(angle)
def torta(t,n):
    t.lt((360/n)/2)
    for i in range(n):
        triangle(t,n,100)
        t.lt(360/n)
bob.fd(100)
torta(bob,6)
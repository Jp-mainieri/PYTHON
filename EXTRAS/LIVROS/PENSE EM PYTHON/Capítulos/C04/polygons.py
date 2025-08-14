import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t,r):

    # circunference = 2 * pi * r
    # circunference = length * n

    length = (r * 2 * 3.14 )/ 20
    
    # r = (length * n) / (2 * pi)
    #r * (2pi) = n * length
    #(r*(2pi))/2 = length

    polygon(t,length,20)

#def arc(angle)
    

square(bob, 200)
polygon(bob, 100, 3)
circle(alice, 100)

turtle.mainloop()
    
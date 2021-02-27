import random
import turtle

scrn = turtle.Screen()
scrn.setup(1000,500)
scrn.setworldcoordinates(0, 0, 1000,500)

fwrds = [i for i in range(10,31)]

s= turtle.Turtle(shape="arrow",visible=False)

a= turtle.Turtle(shape="turtle")
a.color("red")
l= turtle.Turtle(shape="turtle")
l.color("black")
m= turtle.Turtle(shape="turtle")
m.color("pink")
n= turtle.Turtle(shape="turtle")
n.color("yellow")
d= turtle.Turtle(shape="turtle")
d.color("blue")

#speed
a.speed(10)
l.speed(10)
m.speed(10)
n.speed(10)
d.speed(10)

#turtlesetup
a.penup()
l.penup()
m.penup()
n.penup()
d.penup()

a.left(90)
a.forward(400)
a.right(90)

l.left(90)
l.forward(350)
l.right(90)

m.left(90)
m.forward(300)
m.right(90)

n.left(90)
n.forward(250)
n.right(90)

d.left(90)
d.forward(200)
d.right(90)
#turtlesetupends

a.speed(4)
l.speed(4)
m.speed(4)
n.speed(4)
d.speed(4)


#ssetup
s.penup()
s.forward(20)
s.pendown()
s.left(90)
s.forward(500)
s.right(90)

s.penup()
s.forward(800)
s.right(90)

s.pendown()
s.forward(500)


#ssetupends


a.pendown()
l.pendown()
m.pendown()
n.pendown()
d.pendown()

#racesetupends

#distance
fa = 0
fl = 0
fm = 0
fn = 0
fd = 0

contestants = [fa,fl,fm,fn,fd]

while True:
    wa = random.choice(fwrds)
    a.forward(wa)
    fa += wa

    wl = random.choice(fwrds)
    l.forward(wl)
    fl += wl

    wm = random.choice(fwrds)
    m.forward(wm)
    fm += wm

    wn = random.choice(fwrds)
    n.forward(wn)
    fn += wn

    wd = random.choice(fwrds)
    d.forward(wd)
    fd += wd

    if any([fa>820,fl>820,fn>820,fm>820,fd>820]):
        break



winner = max([fa,fl,fm,fn,fd])

if winner == fa:
    print("Red Wins")

if winner == fl:
    print("Black Wins")

if winner == fm:
    print("Pink Wins")

if winner == fn:
    print("yellow Wins")

if winner == fd:
    print("Blue Wins")

turtle.done()

#Brett McKim, created April 28, 2016, submitted May 3, 2016



import turtle
import math


bob = turtle.Turtle()
bob.penup()
bob.setposition(-150,0)
bob.pendown()

bob.left(90)
bob.forward(230)

bob.right(90)
for i in range(17):
    bob.right(10)
    bob.forward(10)

bob.left(170)
for i in range(17):
    bob.right(10)
    bob.forward(10)

#----------------------

bob.penup()
bob.left(170)
bob.forward(150)
bob.left(90)

bob.pendown()
bob.forward(200)
bob.right(160)
bob.forward(110)
bob.left(140)
bob.forward(110)
bob.right(160)
bob.forward(200)


#import turtle

###def drawB(t,width,height):
##    "draw the letter B using t, some width and height"
##    Xstart = t.xcor()
##    Ystart = t.ycor()
##
##    bottomBX = Xstart
##    bottomBX = Ystart - h
##
##    t.forward(width)
##    t.left(90)

#Brett = turtle.Turtle()

##import turtle
##
##def poly(t,n,d):
##    for i in range(n):
##        t.forward(d)
##        t.left(360/n)
##
###----------------------
##t = turtle.Turtle()
##t.color("red")

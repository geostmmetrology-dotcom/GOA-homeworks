from turtle import *

#i want to paint a house
#step1: draw a square
speed(30)
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("green")
begin_fill()
left(90)
forward(100) #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red") #draw a roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("orange")
left(30)
forward(70)
color("white") #draw a window
left(90)
forward(30)

color("blue")
begin_fill()
forward(40)
left(90)
forward(45)
left(90)
forward(40)
left(90)
forward(45)
end_fill()

left(90)  #draw a second window
forward(40)
color("white")
forward(60)

color("blue")
begin_fill()
forward(40)
left(90)
forward(45)
left(90)
forward(40)
left(90)
forward(45)
end_fill()

exitonclick()
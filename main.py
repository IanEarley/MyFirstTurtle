from turtle import *

speed(5)

bgcolor("black")
color("gold")

print("making the sun...")
begin_fill()
circle(60)
end_fill()

penup()
forward(100)
color("grey")
pendown()

print("making mercury...")
begin_fill()
circle(20)
end_fill()

print("making Mars? wait...")
penup()
forward(80)
color("red")
pendown()

begin_fill()
circle(40)
end_fill()

penup()
forward(90)
color("green")
pendown()

begin_fill()
circle(30)
end_fill()
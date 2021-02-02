from turtle import *
from random import randint
import turtle

Screen().bgcolor('#ffeab5')

def drawRec(turtle,x,y,width,height,color):
  turtle.color(color)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.speed(0)

  turtle.begin_fill()
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90) 
  turtle.forward(height)
  turtle.end_fill()

snow = turtle.Turtle() 
drawRec(snow,160,-200,400,900,'#32ffdd') 
snow.speed(0)


penup()
goto(-140,140)
speed(0)
for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  color('#030002')

ada = Turtle()
ada.color('#ffd103')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

ja = Turtle()
ja.color('#ff5303')
ja.shape('turtle')

ja.penup()
ja.goto(-160,75)
ja.pendown()

kr = Turtle()
kr.color('#03c4ff')
kr.shape('turtle')

kr.penup()
kr.goto(-160,50)
kr.pendown()

r = Turtle()
r.color('#9e03ff')
r.shape('turtle')

r.penup()
r.goto(-160,25)
r.pendown()


traffic_light = Turtle()
traffic_light.penup()
traffic_light.goto(-210,140)
traffic_light.pendown()
traffic_light.color('#1d1159')
traffic_light.begin_fill()

for i in range(2):
  traffic_light.forward(60)
  traffic_light.right(90)
  traffic_light.forward(170)
  traffic_light.right(90)

traffic_light.end_fill()

def drawCircle(x,y,rad,color):
  circle = Turtle()
  circle.hideturtle()
  circle.penup()
  circle.goto(x,y)
  circle.color(color)
  circle.begin_fill()
  circle.circle(rad)
  circle.end_fill()

 
drawCircle(-180,85,25,'#ff3a2f') 
drawCircle(-180,30,25,'#fff022') 
drawCircle(-180,-25,25,'#53c22b') 

 

  


for turn in range(100):
  ada.forward(randint(1,5))
  ja.forward(randint(1,5))
  kr.forward(randint(1,5))
  r.forward(randint(1,5))

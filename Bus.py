


import turtle

scr = turtle.Screen()
scr.title("Scl_ Bus")
scr.bgcolor("white")
scr.setup(800,600)

road = turtle.Turtle()
road.color("black")
road.fillcolor("black")
road.begin_fill()
road.penup()
road.goto(-400,0)
road.pendown()
road.hideturtle()
for i in range(2):
    road.fd(800)
    road.rt(90)
    road.fd(200)
    road.rt(90)
road.end_fill()


pen= turtle.Turtle()
pen.pensize(5)
pen.color("yellow")
pen.shape("turtle")
pen.fillcolor("yellow")
pen.begin_fill()
pen.penup()
pen.goto(-200,100)
pen.pendown()

for i in range(2):
    pen.fd(400)
    pen.rt(90)
    pen.fd(200)
    pen.rt(90)
pen.end_fill()
pen.hideturtle()


wheel1 = turtle.Turtle()
wheel1.color("brown")
wheel1.pensize(3)
wheel1.shape("turtle")
wheel1.fillcolor("black")
wheel1.begin_fill()
wheel1.penup()
wheel1.goto(-100,-130)
wheel1.pendown()
wheel1.circle(30)
wheel1.end_fill()
wheel1.hideturtle()

wheel2 = turtle.Turtle()
wheel2.color("brown")
wheel2.pensize(3)
wheel2.shape("turtle")
wheel2.fillcolor("black")
wheel2.begin_fill()
wheel2.penup()
wheel2.goto(100,-130)
wheel2.pendown()
wheel2.circle(30)
wheel2.end_fill()
wheel2.hideturtle()

window = turtle.Turtle()
window.color("lightblue")
window.fillcolor("lightblue")
window.begin_fill()
window.penup()
window.goto(120,15)
window.pendown()
for i in range(4):
    window.fd(75)
    window.lt(90)
window.end_fill()
window.hideturtle()

name = turtle.Turtle()
name.color("Blue")
name.write("MathuMitha",align="center",font=("arial",24,"bold","italic"))
name.hideturtle()





import turtle
import time

col=('yellow','green','cyan','pink','white','violet','orange','indigo','red')

t=turtle.Turtle()
t.width(3)
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(25)

x=1

for i in range(0,35,1):
    for j in range(0,4):
        t.color(col[(0+i+j)%9])
        t.fd(x)
        t.lt(45)
        t.color(col[(1+i+j)%9])
        t.fd(x)
        t.rt(90)
        t.color(col[(2+i+j)%9])
        t.fd(x)
        t.lt(45)
        t.color(col[(3+i+j)%9])
        t.fd(x)
        t.rt(90)
    t.lt(135)
    t.up()
    t.fd(10)
    t.down()
    t.rt(135)
    x=x+4

t.up()
t.goto(-425,-80)
t.down()
t.pencolor('blue')
t.write("THANK YOU!",align='left',font=("Comic Sans MS",100,'bold'))
t.hideturtle()

time.sleep(10)
import turtle
import random
import math


# thiet lap man hinh
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgpic("background.gif")

# thiet lap vung di chuyen
around = turtle.Turtle()
around.hideturtle()
around.penup()
around.setposition(-300 , -300)
around.pendown()
around.pensize(3)
around.speed(0)
for i in range(4):
    around.forward(600)
    around.left(90)

# tao nhan vat anh hung
hero = turtle.Turtle()
screen.addshape("hero.gif")
hero.shape("hero.gif")
hero.penup()

# tao quai vat
monster = turtle.Turtle()
screen.addshape("mon.gif")
monster.shape("mon.gif")
monster.penup()
monster.speed(0)
# thiet lap vi tri random cho quai vat
monster.setposition(random.randint(-300, 300), random.randint(-300, 300))

# thiet lap cac ham di chuyen
speed = 1
def turnleft():
    hero.left(30)
def turnright():
    hero.right(30)
def increaseSpeed():
    global speed
    speed += 1
    if speed >= 5: 
        speed = 5
def decreaseSpeed():
    global speed
    speed -= 1
    if speed <= -5:
        speed = -5

# thiet lap di chuyen khi nhan phim
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up")
turtle.onkey(decreaseSpeed, "Down")

# kiem tra va cham giua anh hung va quai vat
def Collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 80:
        return True
    else: 
        return False
def boundaryChecking(t):
    if t.xcor() < -252 or t.xcor() > 248:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < - 230 or t.ycor() > 230:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))

# xu li khi anh hung cham vao bien
while True:
    # thiet lap anh hung tien ve phia truoc
    hero.forward(speed)
    # kiem tra xem anh hung co cham bien khong?
    boundaryChecking(hero)
    # kiem tra va cham
    if Collision(hero, monster): 
        from turtle import *
        pencolor('red')
        hideturtle()
        write("YOU WIN!", align="center", font=("Cooper Black", 25, "italic"))
        break
    # thiet lap quai vat di chuyen
    monster.forward(6)
    monster.left(random.randint(10, 180))
    boundaryChecking(monster)    
turtle.done()

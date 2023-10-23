import math
import os
import random
import turtle
import winsound

# thiet lap man hinh
screen = turtle.Screen()
# screen.setup(700, 700)
screen.bgpic('background.gif')

# thiet lap vung gioi han di chuyen
around = turtle.Turtle()
around.hideturtle()
around.penup()
around.pensize(3)
around.setposition(-300, -300)
around.pendown()
around.speed(0)
for i in range(4):
    around.forward(600)
    around.left(90)

# tao anh hung
hero = turtle.Turtle()
screen.addshape("hero.gif")
hero.shape("hero.gif")
hero.penup()

# vi tri xuat hien anh hung
hero.setposition(0, -250)
hero.setheading(90)

# toc do anh hung
heroSpeed = 15
# thiet lap toc do dan cua sieu anh hung
bulletSpeed = 20

# tao quai vat
monster = turtle.Turtle()
screen.addshape("monster.gif")
monster.shape("monster.gif")
monster.penup()
monster.speed(0)

# vi tri xuat hien quai vat
monster.setposition(random.randint(-300, 300), random.randint(-100, 300))

# thiet lap toc do 
monsterSpeed = 2

# khoi tao dan
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# trang thai sung cua sieu nhan
bulletState = "ready"

# khoi tao vu khi quai vat
gun = turtle.Turtle()
gun.shape("circle")
gun.color("red")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5, 0.5)
gun.hideturtle()

# thiet lap trang thai sung va toc do dan cua quai vat
bulletState_monster = "ready"
bulletSpeed_monster = 20


# ham xuat hien vu khi sieu nhan
def fire_bullet():
    global bulletState
    if bulletState == "ready":
        winsound.PlaySound('tiengsung.wav', winsound.SND_FILENAME)
        # os.system('tiengsung.wav')
        bulletState = "fire"
        # dat vu khi o truoc nguoi choi
        x = hero.xcor()
        y = hero.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# ham xuat hien vu khi quai vat
def fire_bullet_monster():
    global bulletState_monster
    if bulletState_monster == "ready":
        bulletState_monster = "fire"
        # dat vu khi truoc quai vat
        x = monster.xcor()
        y = monster.ycor() + 10
        gun.setposition(x, y)
        gun.showturtle()


# khoi tao cac phim di chuyen cho sieu nhan
def move_left():
    x = hero.xcor()
    x -= heroSpeed
    if x < -280:
        x = -280
    hero.setx(x)


def move_right():
    x = hero.xcor()
    x += heroSpeed
    if x > 280:
        x = 280
    hero.setx(x)


# khi nhan phim
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.listen()


# ham kiem tra cac doi tuong co va cham nhau khong
def collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


def collision_player(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 130:
        return True
    else:
        return False


# khoi tao diem cua sieu nhan
# ban dau diem bang 0
score = 0
# hien diem len man hinh
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-332, 315)
scoreString = "Player: %s" % score
score_pen.write(scoreString, False, align="left", font=("Arial", 19, "normal"))
score_pen.hideturtle()

# khoi tao diem cua quai vat
score_monster = 0
score_monster_pen = turtle.Turtle()
score_monster_pen.speed(0)
score_monster_pen.color("black")
score_monster_pen.penup()
score_monster_pen.setposition(325, 315)
scoreString_monster = "Enemy: %s" % score_monster
score_monster_pen.write(scoreString_monster, False, align="right", font=("Arial", 19, "normal"))
score_monster_pen.hideturtle()

# main game loop
while True:
    # thiet lap di chuyen quai vat
    x = monster.xcor()
    x += monsterSpeed
    monster.setx(x)
    # goi ham khoi tao vu khi va su dung
    fire_bullet_monster()
    # dieu khien huong di dan cua quai vat
    if bulletState_monster == "fire":
        y = gun.ycor()
        y -= bulletSpeed_monster
        gun.sety(y)

    # kiem tra dan o vi tri botton, neu dung thi an dan
    if gun.ycor() < -275:
        gun.hideturtle()
        bulletState_monster = "ready"

    # di chuyen quai vat len xuong
    if monster.xcor() > 280:
        y = monster.ycor()
        y -= 40
        monster.sety(y)
        monsterSpeed *= -1

    if monster.xcor() < -280:
        y = monster.ycor()
        y -= 40
        monster.sety(y)
        monsterSpeed *= -1

    # kiem tra va cham giua dan cua sieu nhan va quai vat
    if collision(bullet, monster):
        winsound.PlaySound('tiengsungtrungmuctieu.wav', winsound.SND_FILENAME)
        # reset dan
        bullet.hideturtle()
        bulletState = "ready"
        bullet.setposition(0, -400)
        # reset quai vat
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        monster.setposition(x, y)
        # cap nhat diem
        score += 10
        scoreString = "Player: %s" % score
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("Arial", 19, "normal"))
    # kiem tra va cham giua dan cua quai vat va sieu anh hung
    if collision(gun, hero):
        winsound.PlaySound('tiengsungtrungmuctieu.wav', winsound.SND_FILENAME)
        # reset dan
        gun.hideturtle()
        bulletState_monster = "ready"
        bullet.setposition(0, -400)
        # reset quai vat
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        monster.setposition(x, y)
        # cap nhat diem
        score_monster += 10
        scoreString_monster = "Enemy: %s" % score_monster
        score_monster_pen.clear()
        score_monster_pen.write(scoreString_monster, False, align="right", font=("Arial", 19, "normal"))
    # va cham sieu nhan va quai vat
    if collision_player(hero, monster):
        winsound.PlaySound('tiengsungtrungmuctieu.mp3', winsound.SND_FILENAME)
        hero.hideturtle()
        monster.hideturtle()
        from turtle import *

        hideturtle()
        write("   GAME OVER\nYOU ARE LOSE", False, align="center", font=("Cooper Black", 25, "italic"))
        break
    # kiem tra dan cua sieu nhan
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)
    # neu dan cua sieu nhan qua man hinh thi an di
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"

turtle.done()

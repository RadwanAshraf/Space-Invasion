# Turtle Graphics Game
import turtle
import math
import random

#set Screen

wn=turtle.Screen()
wn.bgcolor("black")



#Draw border
border=turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()


#Create Player

player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 30

number_of_enemies = 1
enemies = []


def create_enemy(ind):

    global enemies
    global number_of_enemies
    ind=number_of_enemies-1
    enemies.append(turtle.Turtle())

        #Create Enemy
    enemies[ind].color("red")
    enemies[ind].shape("circle")
    enemies[ind].penup()
    enemies[ind].speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemies[ind].setposition(x,y)


create_enemy(number_of_enemies)
enemyspeed = 3

#Create Bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 60

#difne bullet state
#ready - ready to fire
#fire - bullet is firing

bulletstate="ready"

#move player Left & Right

current=0

def move_left():
     x = player.xcor()
     x -= playerspeed
     if x<-280:
         x=-280
     player.setx(x)
     bullet_movement()
     #enemy_movement()


def move_right():
     x=player.xcor()
     x+=playerspeed
     if x > 280:
         x = 280
     player.setx(x)
     bullet_movement()
    # enemy_movement()


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate="fire"
        bullet_movement()

def is_collesion(t1,t2) :
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        create_enemy(number_of_enemies+1)
        return True
    else:
        return False

#Enemy Movement

def enemy_movement():
    # move enemy
    global enemyspeed
    global bulletstate
    global number_of_enemies
    for enemy in enemies:
        x = enemy.xcor()
        y = enemy.ycor()
        if x > 285:
            y = enemy.ycor()
            y -= 15
            enemy.sety(y)
            enemyspeed *= -1

        if x < -285:
            y = enemy.ycor()
            y -= 15
            enemy.sety(y)
            enemyspeed *= -1

        #Check if there is Collesion
        if is_collesion(bullet,enemy):
                enemy.setposition(-240,250)
                bulletstate = "ready"
                bullet.setposition(0,-400)
                n = number_of_enemies+1
                create_enemy(n)
                return
            # Check if there is Collesion
        if is_collesion(player, enemy):
               enemy.hideturtle()
               player.hideturtle()
               print("Game Over")

        x += enemyspeed
        enemy.setx(x)
        enemy.sety(y)

#Bullet Movement
def bullet_movement():

    global bulletspeed
    global bulletstate

    if bulletstate == "fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
        bullet.showturtle()
    else :
        # move Bullet above player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y)

    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate ="ready"


#game Over



#Key Listen

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet,"space")


#main Game Loop
while True:
    enemy_movement()
    bullet_movement()
  #  create_enemy()




wn.exitonclick()
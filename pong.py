import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)
scorea=0
scoreb=0

paddlea=turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(5,1)
paddlea.penup()
paddlea.goto(-350,0)

paddleb=turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(5,1)
paddleb.penup()
paddleb.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

score=turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("White")
score.penup()
score.goto(0,260)
score.write("PLAYER 1 - 0 PLAYER 2 - 0",align="center",font=("Courier",24,"normal"))

ball.dx= 0.1
ball.dy= 0.1

def paddleaUp():
    paddleay = paddlea.ycor()
    paddleay += 10
    paddlea.sety(paddleay)
    
def paddleaDown():
    paddleay = paddlea.ycor()
    paddleay -= 10
    paddlea.sety(paddleay)

def paddlebUp():
    paddleby = paddleb.ycor()
    paddleby += 10
    paddleb.sety(paddleby)
    
def paddlebDown():
    paddleby = paddleb.ycor()
    paddleby -= 10
    paddleb.sety(paddleby)

wn.listen()
wn.onkeypress(paddleaUp,"w")
wn.onkeypress(paddleaDown,"s")
wn.onkeypress(paddlebUp,"Up")
wn.onkeypress(paddlebDown,"Down")

while True: 
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    ## For top and bottom
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    elif ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    ##For left and right
    if ball.xcor() > 390: 
        ball.goto(0,0)
        ball.dx *= -1
        scorea+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))
        
        
    elif ball.xcor() < -390: 
        ball.goto(0,0)
        ball.dx *= -1
        scoreb+=1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))    
    
    ##Paddle collision
    if ball.xcor() > 330 and ball.ycor() < paddleb.ycor() + 50 and ball.ycor() > paddleb.ycor() - 50: 
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    if ball.xcor() < -330 and ball.ycor() > paddlea.ycor() - 50 and ball.ycor() < paddlea.ycor() + 50: 
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
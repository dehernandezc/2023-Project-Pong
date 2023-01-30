import turtle

wn = turtle.Screen()                            #Pong Project Window Creation
wn.title("Pong by David Hernández")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

marcadorA = 0                                   #Program Scoreboard Variables
marcadorB = 0

jugadorA = turtle.Turtle()                      #Object Attributes: PlayerA
jugadorA.speed(6)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_len=1, stretch_wid=5)

jugadorB = turtle.Turtle()                      #Object Attributes: PlayerA
jugadorB.speed(6)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_len=1, stretch_wid=5)

pelota = turtle.Turtle()                        #Object Attributes: Ball
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

pelota.dx = 1
pelota.dy = 1

division = turtle.Turtle()                      #Object Attributes: Division
division.color("white")
division.goto(0,400)
division.goto(0,-400)

pen = turtle.Turtle()                           #Object Attributes: Scoreboard
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0     Jugador B: 0", align="center", font=("Courier", 25, "normal"))

def jugadorA_up():                              #Player controls
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:                                     #Main game loop
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()

        pen.write(f"Jugador A: {marcadorA}      Jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()

        pen. write (f"Jugador A:  {marcadorA}   Jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal"))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() +50
            and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1
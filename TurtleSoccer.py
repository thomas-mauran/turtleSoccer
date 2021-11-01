import turtle
import time

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Soccer HD edition 2018, by Thomas Mauran")
wn.setup(height = 1.0, width = 1.0)
wn.tracer(0)

# Variables
cursorSize = 20
demiTerrainLongueur = 450
demiTerrainLargeur = 250
butPlayer1 = 0
butPlayer2 = 0
vainqueur = False
delay = 0.01


#Terrain 

def terrain():

    # Terrain turtle

    terrain = turtle.Turtle()
    terrain.speed(10)
    terrain.pu()
    terrain.ht()
    terrain.goto(-demiTerrainLongueur,demiTerrainLargeur)
    terrain.color("white")
    terrain.pd()
    terrain.width(2)

    # Terrain avec surface de reparatiozsn
    for i in range (2): 
        terrain.fd(900)
        terrain.rt(90)
        terrain.fd(150)
        terrain.rt(90)
        terrain.fd(75)
        terrain.lt(90)
        terrain.fd(200)
        terrain.lt(90)
        terrain.fd(75)
        terrain.rt(90)
        terrain.fd(150)
        terrain.rt(90)
    # Cercle central
    terrain.fd(450)
    terrain.rt(90)
    terrain.fd(demiTerrainLargeur)
    terrain.pu()
    terrain.goto(-100,0)
    terrain.pd()
    terrain.circle(100)
    terrain.pu()
    terrain.goto(0,0)
    terrain.pd()
    terrain.fd(demiTerrainLargeur)
    terrain.pu()
    terrain.goto(-demiTerrainLongueur,demiTerrainLargeur)
    terrain.pd()
    terrain.setheading(0)

    # Terrain avec cage 
    for i in range (2): 
        terrain.fd(900)
        terrain.rt(90)
        terrain.fd(200)
        terrain.rt(90)
        terrain.fd(25)
        terrain.lt(90)
        terrain.fd(100)
        terrain.lt(90)
        terrain.fd(25)
        terrain.rt(90)
        terrain.fd(200)
        terrain.rt(90)

    # Bordure du terrain
    terrain.pd()
    for i in range(2):
        terrain.fd(demiTerrainLongueur*2)
        terrain.rt(90)
        terrain.fd(demiTerrainLargeur*2)
        terrain.rt(90)

terrain()

# boule du centre
boule = turtle.Turtle()
boule.shape("circle")
boule.color("white")

# Creation d'un objet player
class Player(turtle.Turtle):
    global cursorSize, demiTerrainLargeur, demiTerrainLongueur
    def __init__(self,color,x,heading):
        turtle.Turtle.__init__(self)
        self.pu()
        self.color(color)
        self.shape("turtle")
        self.shapesize(1.3)
        self.goto(x, 0)
        self.setheading(heading)
        self.vitesse = 3
        self.speed(0)

    def move(self):
        self.forward(self.vitesse)
        if self.xcor() >= demiTerrainLongueur - cursorSize or self.xcor() <= -demiTerrainLongueur + cursorSize:
            self.left(180)
        elif self.ycor() >= demiTerrainLargeur - cursorSize or self.ycor() <= - demiTerrainLargeur + cursorSize:
            self.left(180)
    def rightTurn(self):
        self.right(30)
    def leftTurn(self):
        self.left(30)
    def acceleration(self):
        if self.vitesse < 15:
            self.vitesse += 1
    def deceleration(self):
        if self.vitesse > -15:
            self.vitesse -= 1

    
class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.shape("circle")
        self.shapesize(10)
        self.color("grey")
        self.shapesize(1.3)
        self.speed(10)
        self.setheading(90)
    
    def collisionTerrain(self):
        global butPlayer1, butPlayer2
        if self.ycor() <= 50 and self.ycor() >= -50 and self.xcor() >= demiTerrainLongueur:
            butPlayer1 += 1
            pointsDuMilieu.clear()
            pointsDuMilieu.pu()
            pointsDuMilieu.setx(-80)
            pointsDuMilieu.pd()
            pointsDuMilieu.color("orange")
            pointsDuMilieu.write("GOAL !", align= "left", font = ("RetroComputer", 60, "normal"))
            time.sleep(1.5)
            pointsDuMilieu.color("white")
            pointsDuMilieu.pu()
            pointsDuMilieu.setx(0)
            pointsDuMilieu.pd()
            goal()

        elif self.xcor() <= 50 and self.ycor() >= -50 and self.xcor() <= - demiTerrainLongueur:
            butPlayer2 += 1
            pointsDuMilieu.clear()
            pointsDuMilieu.pu()
            pointsDuMilieu.setx(-80)
            pointsDuMilieu.pd()
            pointsDuMilieu.color("cyan")
            pointsDuMilieu.write("GOAL !", align= "left", font = ("RetroComputer", 60, "normal"))
            time.sleep(1.5)
            pointsDuMilieu.color("white")
            pointsDuMilieu.pu()
            pointsDuMilieu.setx(0)
            pointsDuMilieu.pd()
            goal()

        if self.xcor() >= demiTerrainLongueur - cursorSize:
            self.setheading(180-self.heading())
            self.setx(demiTerrainLongueur - cursorSize*2.5)
        elif  self.xcor() <= -demiTerrainLongueur + cursorSize:
            self.setheading(180-self.heading())
            self.setx(-demiTerrainLongueur + cursorSize*2.5)
        elif self.ycor() >= demiTerrainLargeur - cursorSize:
            self.setheading(180-self.heading())
            self.sety(demiTerrainLargeur - cursorSize*2.5)
        elif self.ycor() <= - demiTerrainLargeur + cursorSize:
            self.setheading(180-self.heading())
            self.sety(-demiTerrainLargeur + cursorSize*2.5)

class TextTurle(turtle.Turtle):
    def __init__(self, x, color):
        turtle.Turtle.__init__(self)
        self.pu()
        self.ht()
        self.speed(0)
        self.goto(x, demiTerrainLargeur + 30)
        self.pd()
        self.color(color)

# Creating player 1
player1 = Player("orange", -demiTerrainLargeur, 0)
# Creating player 2
player2 = Player("cyan", demiTerrainLargeur, 180)

# balle
balle = Ball()

# Creating the player 1 score 
scorePlayer1 = TextTurle(-demiTerrainLargeur, "orange")
scorePlayer1.write(butPlayer1, font=("RetroComputer", 60, "normal"))
# Creating the player 2 score 
scorePlayer2 = TextTurle(demiTerrainLargeur, "cyan")
scorePlayer2.write(butPlayer2, font=("RetroComputer", 60, "normal"))

# :
pointsDuMilieu = TextTurle(0, "white")
pointsDuMilieu.write(":", align="center", font=("RetroComputer", 80, "normal"))

# reset text
resetText = TextTurle(-100, "white")
resetText.pu()
resetText.sety(-300)
resetText.pd()

# Distance beetween the ball and the turtle        
def distance(t1, t2):
    distance1 = t1.distance(t2)
    if distance1 < cursorSize*2:
        t2.setheading(t1.heading())
        t2.fd(cursorSize*4)

# When a player scores
def goal():
    global vainqueur
    player1.goto(-demiTerrainLargeur, 0)
    if butPlayer1 != 0:
        scorePlayer1.clear()
        scorePlayer1.write(butPlayer1, font=("RetroComputer", 60, "normal"))

    player1.vitesse = 3
    
    
    balle.goto(0,0)

    player2.goto(demiTerrainLargeur, 0)
    
    if butPlayer2 != 0:
        scorePlayer2.clear()
        scorePlayer2.write(butPlayer2, font=("RetroComputer", 60, "normal"))
        pointsDuMilieu.color("cyan")
    player2.vitesse = 3

    if butPlayer1 < 5 and butPlayer2 < 5:
        pointsDuMilieu.color("white")
        pointsDuMilieu.clear()
        pointsDuMilieu.write("3", align = "center", font = ("RetroComputer", 70, "normal")) 
        time.sleep(1)
        pointsDuMilieu.clear()
        pointsDuMilieu.write("2", align = "center", font = ("RetroComputer", 70, "normal")) 
        time.sleep(1)
        pointsDuMilieu.clear()
        pointsDuMilieu.write("1", align = "center", font = ("RetroComputer", 70, "normal")) 
        time.sleep(1)
        pointsDuMilieu.clear()
        pointsDuMilieu.write("Go !", align = "center", font = ("RetroComputer", 70, "normal")) 
        time.sleep(1)
        player1.setheading(0)
        player2.setheading(180) 
        pointsDuMilieu.clear()
        pointsDuMilieu.color("white")
        pointsDuMilieu.write(":", align = "center", font = ("RetroComputer", 70, "normal"))     
    elif butPlayer1 == 5:
        pointsDuMilieu.pu()
        pointsDuMilieu.setx(-150)
        pointsDuMilieu.pd()
        pointsDuMilieu.clear()
        pointsDuMilieu.color("orange")
        pointsDuMilieu.write("Le Joueur 1 gagne !", align="left", font=("RetroComputer", 40, "normal"))
        vainqueur = True
        resetText.write("press R to replay", align=("left"), font = ("retrocomputer", 30, "normal"))

    elif butPlayer2 == 5:
        pointsDuMilieu.pu()
        pointsDuMilieu.setx(-150)
        pointsDuMilieu.pd()
        pointsDuMilieu.clear()
        pointsDuMilieu.color("cyan")
        pointsDuMilieu.write("Le Joueur 2 gagne !", align="left", font=("RetroComputer", 40, "normal"))
        vainqueur = True
        resetText.write("press R to replay", align=("left"), font = ("retrocomputer", 30, "normal"))


#def restart function
def restart():
    if vainqueur == True:
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python'] + sys.argv)

wn.listen()

wn.onkey(player1.rightTurn, "d")
wn.onkey(player1.leftTurn, "q")
wn.onkey(player1.acceleration, "z")
wn.onkey(player1.deceleration, "s")


wn.onkey(player2.rightTurn, "Right")
wn.onkey(player2.leftTurn, "Left")
wn.onkey(player2.acceleration, "Up")
wn.onkey(player2.deceleration, "Down")


wn.onkey(restart, "r")


while 1:
    wn.update()
    time.sleep(delay)
    player1.move()
    player2.move()
    balle.collisionTerrain()
    distance(player1, balle)
    distance(player2, balle)
   
    if vainqueur == True:
        break


wn.mainloop()
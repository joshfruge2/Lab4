#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.left(90)
        alice.backward(100)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    
def squaresInSquares(steve, num_squares):
    pen = turtle.Turtle()    
    side_length = 200
    decrement = side_length / num_squares  
    for i in range(num_squares):
        for _ in range(4):
            pen.forward(side_length)
            pen.right(90)
        pen.penup()
        pen.goto(pen.xcor() + decrement / 2, pen.ycor() - decrement / 2)
        pen.pendown()
        side_length -= decrement
        

def main():
    myTurtle = turtle.Turtle()
    
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 4) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

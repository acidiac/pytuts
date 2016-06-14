import turtle 
import random

ninja = turtle.Turtle()

ninja.speed(0)

for i in range(180):
    col = ['#ff0c43', '#0099ff', '#ff3461', '#4eb8ff', '#ff5b80', '#ffff27', '#ffff62']
    ninja.pencolor(random.choice(col))
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
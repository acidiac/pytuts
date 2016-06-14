import turtle

draw = turtle.Turtle()

side = int(input("gimme the length of a side: "))

draw.forward(side)
draw.right(90)     # Rotate clockwise by 90 degrees

draw.forward(side)
draw.right(90)

draw.forward(side)
draw.right(90)

draw.forward(side)
draw.right(90)

turtle.done()
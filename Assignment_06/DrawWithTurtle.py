import turtle
import math


colors = ["purple", "blue", "green", "yellow", "orange", "red"]

pen = turtle.Pen()
pen.shape("turtle")

index = 0
jump = 20
length = 20
preInternal = 0

for i in range(3, 13):

    # We check the index and if it has reached the end of the colors list,
    # we reset the index to zero to reuse the colors.
    if index >= len(colors):
        index = 0
        pen.color(colors[index])
    else:
        pen.color(colors[index])

    # In order not to see the pen on the page,
    # we use the following commands.
    pen.penup()
    pen.goto(jump, 0)
    pen.pendown()

    internalAngle = ((i - 2) * 180) / i                         # The internal angle of the polygon.
    rotate = 180 - ((internalAngle / 2) + (preInternal / 2))    # Calculate first rotate.
    length = 2 * jump * math.sin(math.radians(180/i))           # Calculate the length of each side.

    for j in range (i):
        pen.left(rotate)
        pen.forward(length)
        rotate = 180 - internalAngle    # Calculate external angle for next rotations in each polygon.

    index += 1 
    jump += 20
    preInternal = internalAngle

pen.done()
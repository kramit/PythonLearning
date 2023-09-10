import turtle

turtle.speed(0)  # Fastest speed
length = 50
angle = 36
shift = 125
repeats = 4  # Choose the number of repeats for the pattern

for drawing in range(repeats):
    for drawing in range(6):
        turtle.forward(length)
        turtle.backward(length)
        turtle.left(angle)
    turtle.penup()
    turtle.left(144)
    turtle.forward(shift)
    turtle.pendown()

turtle.done()

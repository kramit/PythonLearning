import turtle

def draw_spoke(length, angle):
    turtle.forward(length)
    turtle.backward(length)
    turtle.left(angle)

def draw_basic_element(length, angle):
    for _ in range(6):
        draw_spoke(length, angle)
        

def draw_frieze_pattern(repeats, length, angle, shift):
    for _ in range(repeats):
        draw_basic_element(length, angle)
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(shift)
        turtle.pendown()

def main():
    turtle.speed(0)  # Fastest speed
    length = 50
    angle = 36
    shift = 125
    repeats = 4  # Choose the number of repeats for the pattern

    draw_frieze_pattern(repeats, length, angle, shift)
    turtle.done()

if __name__ == "__main__":
    main()

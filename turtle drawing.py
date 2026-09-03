import turtle

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(3)
t.pensize(4)

# Requirement 5: A variable to control line measurements
line_length = 40

# === SECTION 1: Colorful Staircase ===
# Requirement 3: Move to starting position without drawing
t.penup()
t.goto(-200, -100)
t.pendown()

# Requirement 1 & 4: Drawing lines using both left() and right()
# Requirement 2: Using the first two colors (red and blue)
# This loop runs 6 times, drawing 2 lines per turn (12 lines total)
for _ in range(6):
    t.color("red")
    t.forward(line_length)
    t.left(90)

    t.color("blue")
    t.forward(line_length)
    t.right(90)

# === SECTION 2: Separate Triangle ===
# Requirement 3: Use penup() and pendown() to make an unconnected section
t.penup()
t.goto(50, 50)
t.pendown()

# Requirement 2: Using a third color (green)
t.color("green")

# Drawing a triangle (3 lines)
# Total visible lines in the drawing: 12 (staircase) + 3 (triangle) = 15 lines
for _ in range(3):
    t.forward(line_length * 2)  # Modifying the measurement variable
    t.left(120)

# Hide turtle and finish
t.hideturtle()
turtle.done()
#outcome stairs with a triangle.
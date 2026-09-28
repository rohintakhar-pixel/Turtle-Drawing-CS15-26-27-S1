from turtle import *

# My drawing is a house

# walls
color("brown")
forward(house_size)
right(90)
forward(house_size)
right(90)
forward(house_size)
right(90)
forward(house_size)
right(90)

# roof
color("red")
left(45)
forward(roof_length)
right(90)
forward(roof_length)
left(45)

# door
penup()
right(90)
forward(house_size)
right(90)
forward(120)
right(90)
pendown()
color("blue")
forward(door_height)
right(90)
forward(door_width)
right(90)
forward(door_height)
right(90)
forward(door_width)

# window
penup()
right(90)
forward(120)
pendown()
color("yellow")
forward(window_size)
right(90)
forward(window_size)
right(90)
forward(window_size)
right(90)
forward(window_size)

# chimney
penup()
right(90)
forward(80)
right(90)
forward(80)
left(90)
pendown()
color("gray")
forward(chimney_height)
right(90)
forward(chimney_width)
right(90)
forward(chimney_height)
right(90)
forward(chimney_width)

done()

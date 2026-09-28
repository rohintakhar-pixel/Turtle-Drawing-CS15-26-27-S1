from turtle import *

house_size = 200
roof_length = house_size * 0.7071
door_width = 40
door_height = 70
window_size = 40
chimney_width = 30
chimney_height = 50

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

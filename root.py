from turtle import *

# hello
letter_size = 30
gap = 10

penup()

# Account for 'H' and 'e' and the gaps between them
backward_length = (letter_size * 2) + (gap * 2)

backward(backward_length)

# H
pendown()
left(90)
forward(letter_size * 2)
backward(letter_size)
right(90)
forward(letter_size)
left(90)
forward(letter_size)
backward(letter_size * 2)
right(90)
penup()
forward(gap)

# e
pendown()
left(90)
forward(letter_size)
right(90)
forward(letter_size)
right(90)
forward(letter_size / 2)
right(90)
forward(letter_size)
left(90)
forward(letter_size / 2)
left(90)
forward(letter_size)
penup()
forward(gap)

# l
pendown()
left(90)
forward(letter_size * 2)
right(90)
penup()
forward(gap)

# l
pendown()
right(90)
forward(letter_size * 2)
left(90)
penup()
forward(gap)

# o
pendown()
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)

done()

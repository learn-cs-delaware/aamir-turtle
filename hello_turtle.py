from turtle import *

my_turtle = Turtle()

# 1. Make the turtle move in a circle/square
# my_turtle.circle(50)

# 2. Make the turtle loop 5 times

my_turtle.speed(1)
for i in range(1,6):
    my_turtle.forward(50)
    for j in range(2,10):
        my_turtle.right(30)
        my_turtle.forward(10)

# 3. Make the turtle loop forever

# 4. Make the turtle go forwards/backwards

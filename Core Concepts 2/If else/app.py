import turtle

get_Turtle = turtle.Turtle()

def square():
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)

elephant_weight = 3000
ant_weight = 0.1

if elephant_weight < ant_weight:
    square()
else:
    get_Turtle.forward(100)

# print(3000 < 0.1)
import turtle

get_Turtle = turtle.Turtle()
get_Turtle.speed(10)

def square():
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)
    get_Turtle.right(90)
    get_Turtle.forward(100)

for count in range(4):
    square()


for count in range(10):
    print(count)
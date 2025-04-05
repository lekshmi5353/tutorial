import turtle

pentagon_turtle = turtle.Turtle()
pentagon_turtle.speed(2)
pentagon_turtle.color("blue")


for _ in range(5):
    pentagon_turtle.forward(100)
    pentagon_turtle.right(72)  


turtle.done()
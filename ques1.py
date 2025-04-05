import turtle


star_turtle = turtle.Turtle()
star_turtle.speed(2)
star_turtle.color("gold")


for i in range(5):
    star_turtle.forward(100)  
    star_turtle.right(144)   

turtle.done()

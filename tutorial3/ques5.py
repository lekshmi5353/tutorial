import turtle


pattern_turtle = turtle.Turtle()
pattern_turtle.speed(2)
pattern_turtle.color("purple")


def draw_hexagon():
    for _ in range(6):
        pattern_turtle.forward(50)
        pattern_turtle.right(60)


for _ in range(10):
    draw_hexagon()
    pattern_turtle.right(36)  


turtle.done()

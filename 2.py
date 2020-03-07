import turtle
brad=turtle.Turtle()
def draw_aquare():
    window=turtle.Screen()
    window.bgcolor("white")
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    for i in range(4):
        brad.forward(100)
        brad.right(90)
        i+=1
draw_aquare()
print(123)

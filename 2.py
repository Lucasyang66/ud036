import turtle
brad=turtle.Turtle()
def draw_aquare():
    window=turtle.Screen()
    window.bgcolor("white")
    brad.shape("turtle")
    brad.color("white")
    brad.speed(5)
    brad.setposition(-150, 0)
    brad.color("blue")
    for i in range(36):
        brad.forward(300)
        brad.right(120)
        i+=1
        for j in range(0,10,2):
            brad.right(10)
            j+=1
       
draw_aquare()

import turtle

def square(brad):
    for i in range(1,5):
        brad.forward(100)
        brad.right(90)
def final():
    window = turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.color("blue")
    brad.shape("turtle")
    brad.speed(10)
    for i in range(1,25):
        square(brad)
        brad.right(15)
    brad.right(90)
    brad.forward(200)
    window.exitonclick()
final()                   

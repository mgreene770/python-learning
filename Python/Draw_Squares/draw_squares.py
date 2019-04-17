import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")    

    draw_square()
    #draw_circle()
    #draw_triangle()

    window.exitonclick()
    
def draw_square():
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    for y in range(1, 73):    
        for i in range(1, 5):
            brad.forward(100)
            brad.right(90)
        brad.right(5)
        
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(1)
    angie.circle(100)
    
def draw_triangle():
    fred = turtle.Turtle()
    fred.speed(50)
    fred.shape("circle")
    fred.color("green")

    for i in range(1, 4):
        fred.forward(100)
        fred.right(120)

        
    

draw_shapes()

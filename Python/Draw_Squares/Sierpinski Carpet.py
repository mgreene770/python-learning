import turtle
import time

def draw_recursion(turtle,edge_length,remaining_recursions, color):

    #save original co-ordinates (didn't know at the time you could use turtle.pos()[0] for X, [1] for Y)
    xcor = turtle.xcor()
    ycor = turtle.ycor()

    #always draw the middle as a filled square
    turtle.penup()
    turtle.setposition(xcor+edge_length,ycor+edge_length)
    turtle.pendown()
    #print ("position x:", turtle.pos()[0], " y: ", turtle.pos()[1])
    turtle.begin_fill()
    turtle.color(color)
    for x in range(4):
        turtle.forward(edge_length)
        turtle.right(90)
    turtle.end_fill()

    # reset to bottom/right
    turtle.penup()
    turtle.setposition(xcor, ycor)
    turtle.pendown()

    if remaining_recursions > 0:
        #bottom left
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        # move up
        turtle.penup()
        turtle.setposition(turtle.xcor(),turtle.ycor()+edge_length)
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        # move up (top left)
        turtle.penup()
        turtle.setposition(turtle.xcor(),turtle.ycor()+edge_length)
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        # move right (top/middle)
        turtle.penup()
        turtle.setposition(turtle.xcor()+edge_length,turtle.ycor())
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        # move down twice, skip middle (bottom/middle)
        turtle.penup()
        turtle.setposition(turtle.xcor(),turtle.ycor()-edge_length-edge_length)
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        #move right (bottom right)
        turtle.penup()
        turtle.setposition(turtle.xcor()+edge_length,turtle.ycor())
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        #move up
        turtle.penup()
        turtle.setposition(turtle.xcor(),turtle.ycor()+edge_length)
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        # move up (top/right)
        turtle.penup()
        turtle.setposition(turtle.xcor(),turtle.ycor()+edge_length)
        turtle.pendown()
        draw_recursion(turtle,edge_length/3,remaining_recursions-1, next_color(remaining_recursions-1))

        #reset to original bottom/right position.
        turtle.penup()
        turtle.setposition(xcor, ycor)
        turtle.pendown()

def draw_sierpinskis_square(iterations):

    edge_length = 400
    start_position_y = -160
    start_position_x = -160

    window = turtle.Screen()
    window.bgcolor("white")
    foo = turtle.Turtle()
    foo.shape("arrow")
    foo.speed("fastest")

    foo.penup()
    foo.setposition(start_position_x, start_position_y)
    foo.pendown()

    foo.left(90)

    for i in range(1, 5):
        foo.forward(edge_length)
        foo.right(90)

    draw_recursion(foo, edge_length/3, iterations-1, next_color(iterations-1))

    window.exitonclick()

def next_color(iterations):
    if iterations == 0:
        return "black"
    elif iterations == 1:
        return "red"
    elif iterations == 2:
        return "yellow"
    else:
        return "blue"

draw_sierpinskis_square(5)

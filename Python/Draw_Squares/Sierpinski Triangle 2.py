import turtle
PROGNAME = 'Sierpinski Triangle'
#Credits: This code was written by editing the code from http://www.lpb-riannetrujillo.com/blog/python-fractal/
#changed from drawing multiple triangle to 'removing' triangles using a white fill.
myPen = turtle.Turtle()
myPen.ht()
myPen.speed(100)
myPen.pencolor('orange')
myPen.color('black')
#points = [[-175,-125],[0,175],[175,-125]] #size of triangle
points = [[-400,-325],[0,375],[400,-325]] #size of triangle

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def main(points,depth):

    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.begin_fill()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])
    myPen.end_fill()

    if depth>0:
        triangle(points, depth-1)
##        triangle([points[1],
##                        getMid(points[0], points[1]),
##                        getMid(points[1], points[2])],
##                   depth-1)
##        triangle([points[2],
##                         getMid(points[2], points[1]),
##                         getMid(points[0], points[2])],
##                   depth-1)
    turtle.Screen().exitonclick()
        
def triangle(points,depth):
    global myPen
    myPen.color('white')

    myPen.up()
    myPen.goto(points[0][0],points[0][1])

    
    myPen.goto(getMid(points[0],points[1]))
    myPen.down()
    myPen.begin_fill()
    myPen.goto(getMid(points[1],points[2]))
    myPen.goto(getMid(points[2],points[0]))
    myPen.end_fill()
    
##    print("depth", depth, "points", points)
##    myPen.down()
##    myPen.begin_fill()
##    myPen.goto(points[1][0],points[1][1])
##    myPen.goto(points[2][0],points[2][1])
##    myPen.goto(points[0][0],points[0][1])
##    myPen.end_fill()
    
    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)


main(points,4)

# 3D Lego Bricks Animation using Glowscript - www.101computing.net/3D-Lego-bricks

cube1 = box(color=vector(1,0,0), pos=vector(0,0,0), length=2, height=2, width=1.5, opacity=1)
stud1 = cylinder(color=vector(1,0,0),pos=vector(0.5,0.5,0.75), axis=vector(0,0,0.3), radius=0.4)
stud2 = cylinder(color=vector(1,0,0),pos=vector(0.5,-0.5,0.75), axis=vector(0,0,0.3), radius=0.4)
stud3 = cylinder(color=vector(1,0,0),pos=vector(-0.5,-0.5,0.75), axis=vector(0,0,0.3), radius=0.4)
stud4 = cylinder(color=vector(1,0,0),pos=vector(-0.5,0.5,0.75), axis=vector(0,0,0.3), radius=0.4)

brick = compound([cube1,stud1,stud2,stud3,stud4])

theta=0.1
framerate=20

while True:
  rate(framerate)
  brick.rotate(angle=theta, axis=vector(1,1,1), origin=vector(0,0,0))

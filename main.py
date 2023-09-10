import turtle

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def bsquare(size):
  for i in range(4):
    turtle.color("red")
    turtle.forward(size)
    turtle.left(90)

def triangle(size):
  for i in range(3):
    turtle.color("blue")
    turtle.forward(size)
    turtle.left(120)
    
def move(len):
  back(-1 * len)

def polygon(sides, len):
  for i in range(sides):
    turtle.color("green")
    turtle.forward(len)
    turtle.left(360 / sides)
    
# for n in range(3, 10):
#   move(50)
#   polygon(n, 100 / n)
#   back(50)
#   turtle.right(360 / 7)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)

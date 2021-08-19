import turtle
t = turtle.Turtle()
t.pencolor("green")
t.speed(0)
#t.forward(100)
t.pensize(1)
for i in range(1000):
  t.forward(100+i)
  t.right(179)
  t.pencolor(i, 90, 90)

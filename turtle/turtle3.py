import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
for i in range(1000):
  t.pencolor(i,78,255-i)
  t.forward(175)
  t.right(181)

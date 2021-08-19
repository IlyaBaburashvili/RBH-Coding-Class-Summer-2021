import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
for i in range(1000):
  t.pencolor(190-i,i,255-i)
  t.forward(150)
  t.right(211)

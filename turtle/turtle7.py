import turtle
t = turtle.Turtle()
t.pencolor("green")
t.speed(0)
#t.forward(100)
t.pensize(1)
for i in range(2000):
  t.forward(i%101)
  t.right(179)
  if i%2==0:
    t.pencolor(i%23, 180-i, 255-i)
  else:
    t.pencolor(255-i, i%4, 167%i)

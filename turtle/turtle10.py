import turtle
t = turtle.Turtle()
t.pencolor("green")
t.speed(0)
#t.forward(100)
t.pensize(1)
for i in range(1,2000000):
  t.forward(23+i)
  t.right(199)
  if i%4==0:
    t.pencolor(i, i%29, 255-i)
  else:
    t.left(3%1)
    t.pencolor(199-i, 23%i, 0)

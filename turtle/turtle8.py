import turtle
t = turtle.Turtle()
t.pencolor("green")
t.speed(0)
#t.forward(100)
t.pensize(1)
for i in range(2000000):
  t.forward(23+i)
  t.right(1)
  t.left(197)
  if i%4==0:
    t.pencolor(i, i%29, 255-i)
  elif i%3==0:
    t.right(4)
    t.pencolor(255, i%57, i)
  else:
    t.pencolor(199-i, 23%i, 0)

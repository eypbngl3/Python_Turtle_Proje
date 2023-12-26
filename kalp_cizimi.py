import turtle as t
t.hideturtle()
t.pensize(5)

# Move to the starting position
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart shape
t.begin_fill()
t.fillcolor("red")
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()


# Keep the window open
t.done()

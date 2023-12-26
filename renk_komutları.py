from turtle import *
color("red","blue")
pensize(5)
def ucgen():
    for x in range(3):
        forward(200)
        left(120)


begin_fill()
print(ucgen())
end_fill()
open()
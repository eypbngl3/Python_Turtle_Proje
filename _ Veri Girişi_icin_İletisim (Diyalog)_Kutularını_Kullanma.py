from turtle import *
N =int(numinput("POLİGON","kenar sayisi"))
renk = textinput("renk","iç rengi")

pensize(4)

begin_fill()
fillcolor(renk)
print(circle(100,360,N))
end_fill()
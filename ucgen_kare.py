from turtle import *


def kareCizim(mesafe): # kare cizim fonksiyonu
    for a in range(1,5):
        forward(mesafe)
        left(90)

hideturtle()
pensize(2)

x= int(input("Kare sayisi gir :  "))
for a in range(x):
    print(kareCizim(50*a))



# üçgem çizim
for b in range(1,4):
    forward(200)
    print(lt(120))

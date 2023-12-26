import turtle as t
print(t.getshapes()) # hangi şekiller var diye öğrenebiliriz.
print(t.shape("turtle")) # kaplumbağa getirir hareket yaparsak kaplumbağa hareket eder.
print(t.fd(200))


print(t.shape("circle"))
print(t.rt(90))
print(t.fd(200))# 200 gider kareye dönüşür.



print(t.shape("square"))
t.hideturtle() # simgeyi kaybeder
t.rt(90)
t.fd(100)
t.showturtle()




t.done()
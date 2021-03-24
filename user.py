from vector import Vector
from punto import Punto
from poligono import Poligono

flag = True
test_number = 0
puntos = []
while(flag):
    test_text = input ("Introduce numero de lados: ")
    test_number = int(test_text)
    if(test_number>2):
        flag=False

for i in range(0, test_number):
    test_text = input ("Introduce x del punto " + i + ": ")
    x = int(test_text)
    test_text = input ("Introduce y del punto " + i + ": ")
    y = int(test_text)
    puntos.append(Punto(x,y))


poligono = Poligono(puntos)



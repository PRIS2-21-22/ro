from punto import Punto
from poligono import Poligono
from linea import Linea

def crearpoligono():
    flag = True
    test_number = 0
    puntos = []
    while(flag):
        test_text = input ("Introduce numero de lados: ")
        test_number = int(test_text)
        if(test_number>2):
            flag=False

    for i in range(0, test_number):
        test_text = input ("Introduce x del punto " + str(i) + ": ")
        x = int(test_text)
        test_text = input ("Introduce y del punto " + str(i) + ": ")
        y = int(test_text)
        puntos.append(Punto(x,y))

    poligono = Poligono(puntos)
    poligono.tostring()
    print("El centroide es: ",poligono.centroide())
    flag = poligono.concavo()
    if flag:
        print("Es concavo")
    else:
        print("Es convexo")

def testlineas():
    linea1 = Linea()
    linea2 = Linea()
    linea1.pendienteordenada(1,3)
    linea2.coeficientes(1,4,9)
    p1 = Punto(1,1)
    p2 = Punto(2,2)
    linea3 = Linea()
    linea3.dospuntos(p1,p2)
    print(linea1.devolverrepresentacion())
    print(linea2.devolverrepresentacion())
    print(linea3.devolverrepresentacion())
    if linea1.interseccion(linea2):
        print("Son secantes")
    else:
        print("Son paralelas")


crearpoligono()
testlineas()






from vector import Vector
from punto import Punto

class Poligono:

    def __init__(self, vertices):
        """Metodo constructor."""
        self.vertices= vertices

    def concavo(self):
        i=0
        vec1 = Vector(self.vertices[i], self.vertices[(i+1)%len(self.vertices)])
        vec2 = Vector(self.vertices[(i+1)%len(self.vertices)], self.vertices[(i+2)%len(self.vertices)])
        prodvectorial = vec1.productovectorial(vec2)
        positivo = prodvectorial >=0

        for i in range(0, len(self.vertices)):
            vec1 = Vector(self.vertices[i], self.vertices[(i+1)%len(self.vertices)])
            vec2 = Vector(self.vertices[(i+1)%len(self.vertices)], self.vertices[(i+2)%len(self.vertices)])
            prodvectorial = vec1.productovectorial(vec2)
            flag = prodvectorial >=0
            if positivo != flag:
                return True

        vec1 = Vector(self.vertices[(i+1)%len(self.vertices)], self.vertices[0])
        prodvectorial = vec2.productovectorial(vec1)
        if positivo != (prodvectorial >=0):
            return True
        return False

    def centroide(self):
        x=0
        y=0
        z=0

        for k in range(1,len(self.vertices)):
            z += (self.vertices[k].get_x()*self.vertices[(k+1)%len(self.vertices)].get_y() - self.vertices[k].get_y()*self.vertices[(k+1)%len(self.vertices)].get_x())
        z=z/2

        for k in range(1,len(self.vertices)):
            x += (self.vertices[k].get_x()+self.vertices[(k+1)%len(self.vertices)].get_x()) * ((self.vertices[k].get_x()*self.vertices[(k+1)%len(self.vertices)].get_y()) - (self.vertices[(k+1)%len(self.vertices)].get_x()*self.vertices[k].get_y()))
        x = x/(6*z)
        for k in range(1,len(self.vertices)):
            y += (self.vertices[k].get_y()+self.vertices[(k+1)%len(self.vertices)].get_y()) * ((self.vertices[k].get_x()*self.vertices[(k+1)%len(self.vertices)].get_y()) - (self.vertices[(k+1)%len(self.vertices)].get_x()*self.vertices[k].get_y()))
        y = y/(6*z)

        return Punto(x,y).tostring()

    def triangular(self,posicion_vertice):
        vertices = []
        vertices.append(self.vertices[posicion_vertice-1])
        vertices.append(self.vertices[posicion_vertice])
        if posicion_vertice == (len(self.vertices)-1):
            vertices.append(self.vertices[0])
        else:
            vertices.append(self.vertices[posicion_vertice+1])
        return Poligono(vertices) 
    def triangulacion(self,poligono):
        i=0
        triangulos = []
        for i in range(0, len(self.vertices)):
            triangulos.append(self.triangular(i))
        return triangulos

    def tostring(self):
        print("Puntos del poligono:")
        for i in range (0,len(self.vertices)):
            print("Punto " + str(i) + " : " + self.vertices[i].tostring())



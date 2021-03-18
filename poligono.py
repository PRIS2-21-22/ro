import vector
import punto

class Poligono:

    def __init__(self, puntos):
        self.puntos = puntos

    def concavo(self):
        i=0
        vec1 = vector.Vector(self.puntos[i], self.puntos[i+1])
        vec2 = vector.Vector(self.puntos[i+1], self.puntos[i+2])
        prodvectorial = vec1.productovectorial(vec2)
        positivo = prodvectorial >=0

        for i in range(0, self.puntos.size)
            vec1 = vector.Vector(self.puntos[i], self.puntos[i+1])
            vec2 = vector.Vector(self.puntos[i+1], self.puntos[i+2])
            prodvectorial = vec1.productovectorial(vec2)
            if(positivo != (prodvectorial >=0)
                return true

        vec1 = vector.Vector(self.puntos[i+1], self.puntos[0])
        prodvectorial = vec2.productovectorial(vec1)
        if(positivo != (prodvectorial >=0)
            return true
        return false

    def centroide(self):
        x,y,z=0.0

        for k in range(0,self.puntos):
            z+=self.puntos[k].get_x*self.puntos[(k+1)%self.puntos].get_y - self.puntos[k].get_y*self.puntos[(k+1)%self.puntos].get_x
        z=z/2

        for k in range(0,self.puntos):
            x+=self.puntos[k].get_x*self.puntos[(k+1)%self.puntos].get_x*self.puntos[k].get_x*self.puntos[(k+1)%self.puntos].get_y - self.puntos[(k+1)%self.puntos].get_x*self.puntos[k].get_y
        x=x/(6*z)

        for k in range(0,self.puntos):
            y+=self.puntos[k].get_x*self.puntos[(k+1)%self.puntos].get_x*self.puntos[k].get_x*self.puntos[(k+1)%self.puntos].get_y - self.puntos[(k+1)%self.puntos].get_x*self.puntos[k].get_y
        y=y/(6*z)

        return punto.Punto(x,y)



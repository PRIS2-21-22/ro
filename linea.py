
class Linea:

    def __init__(self):
        """Metodo constructor."""
        self.x = 0
        self.y = 0
        self.pendiente = 0

    def dospuntos(self,p1,p2):
        coeficiente = (p2.get_y()-p1.get_y())/(p2.get_x()-p1.get_x())
        self.representacion = "0 = " + str(coeficiente) + "*x - y + " + str(coeficiente*(-p1.get_x()) - p1.get_y())
        self.pendiente = (p2.get_y()-p1.get_y())/(p2.get_x()-p1.get_x())

    def pendienteordenada(self,m,b):
        self.representacion = "0 = " + str(m) + "*x  - y + " + str(b)
        self.pendiente = m

    def pendientepunto(self,m,x1,y1):
        self.representacion = "0 = " + str(m) + "*x - y " + str(y1 - m*x1)
        self.pendiente = m

    def coeficientes(self,a,b,c):
        self.representacion = "0 = " + str(a) + "*x + " + str(b) + "*y + " + str(c)
        self.pendiente = -a/b

    def vertical(self,x0):
        self.representacion = "0 = " + str(x0) + "- x"
        self.pendiente = 0

    def horizontal(self,y0):
        self.representacion = "0 = " + str(y0) + "- y"
        self.pendiente = 0

    def interseccion(self, linea):
        if self.pendiente == linea.pendiente:
            return 0
        else:
            return 1

    def devolverrepresentacion(self):
        return self.representacion


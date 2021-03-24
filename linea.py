
class Linea:

    def __init__(self):
         """El constructor no acepta por
        parametro nada
        """
        self.x = 0
        self.y = 0
        self.pendiente = 0

    def dospuntos(self,p1,p2):
        self.representacion = "0 = [" + p2.get_y + "-" + p1.get_y +")/(" + p2.get_x + "-" + p1.get_x + ")]*(x-" + p1.get_x + ")+" + p1.get_y
        self.pendiente = (p2.get_y-p1.get_y)/(p2.get_x-p1.get_x)

    def pendienteordenada(self,m,b):
        self.representacion = "0 = " + m + "*x+" + b + "- y"
        self.pendiente = m

    def pendientepunto(self,m,p1):
        self.representacion = "0 = " + m + "*(x-" + p1.get_y + ")+" + p1.get_y + "- y"
        self.pendiente = m

    def coeficientes(self,a,b,c):
        self.representacion = "0 = " + a + "*x+" + b + "*y+" + "c"
        self.pendiente = -a/b

    def vertical(self,x0):
        self.representacion = "0 = " + x0 + "- x"
        self.pendiente = 0

    def horizontal(self,y0):
        self.representacion = "0 = " + y0 + "- y"
        self.pendiente = 0

    def interseccion(self, linea):
        if self.pendiente == linea.pendiente:
            return 0
        else:
            return 1

    def devolverrepresentacion(self):
        return self.representacion


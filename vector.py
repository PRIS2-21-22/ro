import math

class Vector:

    def __init__(self, punto1 ,punto2):
        "Inicia con los dos puntos"
        self.punto1= punto1
        self.punto2 = punto2

    def coordenadax(self):
        return self.punto2.get_x() - self.punto1.get_x()

    def coordenaday(self):
        return self.punto2.get_y() - self.punto1.get_y()

    def modulo(self):
        return math.sqrt(math.pow(self.coordenadax,2)+ math.pow(self.coordenaday,2))

    def productovectorial(self,vector):
        return self.coordenadax()*vector.coordenaday()- self.coordenaday*vector.coordenadax()


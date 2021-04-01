class Punto:
    def __init__(self, x, y):
        """Function that does something interesting.

        Args:
            - input - Input of the function

        Returns:
            - output - Output of the function
        """
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self,aux):
        self.x = aux

    def set_y(self,aux):
        self.y = aux

    def tostring(self):
        return "X=" + str(self.x) +", Y=" + str(self.y)



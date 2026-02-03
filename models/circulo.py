from models.shape import Shape
import math

class Circulo(Shape):
    def __init__(self, raio:int):
        self._shape = "Círculo"
        self._raio = raio
        Shape.lista_shapes.append(self)
    

    def area(self):
        return round(math.pi * (self._raio**2), 2)


    def comprimento(self):
        return round(math.pi * (2 * self._raio), 2)

from models.shape import Shape

class Quadrado(Shape):
    def __init__(self, lado:int):
        self._shape = "Quadrado"
        self._lado = lado
        Shape.lista_shapes.append(self)

    def area(self):
        return self._lado**2
    
    def comprimento(self):
        return 4 * self._lado

from models.shape import Shape

class Triangulo(Shape):
    """
    Considere lado B como a base do triângulo
    """

    def __init__(self, ladoA:int, ladoB:int, ladoC:int, altura:int):
        self._shape = "Triângulo"
        self._ladoA = ladoA
        self._ladoB = ladoB
        self._ladoC = ladoC
        self._altura = altura
        Shape.lista_shapes.append(self)
    

    def area(self):
        return round((self._ladoB * self._altura) / 2, 2)
    
    
    def comprimento(self):
        return self._ladoA + self._ladoB + self._ladoC

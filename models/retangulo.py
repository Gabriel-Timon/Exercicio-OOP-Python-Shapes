from models.shape import Shape

class Retangulo(Shape):
    def __init__(self, base:int, altura:int):
        self._shape = "Retângulo"
        self._base = base
        self._altura = altura
        Shape.lista_shapes.append(self)
    

    def area(self):
        return self._base * self._altura
    

    def comprimento(self):
        return (self._base * self._altura) * 2
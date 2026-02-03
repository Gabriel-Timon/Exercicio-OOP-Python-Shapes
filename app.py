from models.circulo import Circulo
from models.quadrado import Quadrado
from models.retangulo import Retangulo
from models.triangulo import Triangulo
from models.shape import Shape

shape1 = Quadrado(5)
shape2 = Circulo(8)
shape3 = Retangulo(4, 10)
shape4 = Triangulo(7, 14, 9, 7)

def main():
    Shape.listar_todos_comprimentos()
    print("\n\n")
    Shape.listar_areas_totais()


if __name__ == "__main__":
    main()

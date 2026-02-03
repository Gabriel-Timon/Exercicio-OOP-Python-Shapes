from models.circulo import Circulo
from models.quadrado import Quadrado
from models.retangulo import Retangulo
from models.triangulo import Triangulo
from models.shape import Shape
from os import system

shape1 = Quadrado(5)
shape2 = Circulo(8)
shape3 = Retangulo(4, 10)
shape4 = Triangulo(7, 14, 9, 7)

def main():
    print("1. Ver o comprimento de todos os shapes")
    print("2. Ver a área de todos os shapes\n")

    opcao = input("Opção: ").strip()

    if opcao.isdigit() and (opcao == "1" or opcao == "2"):
        print()
        match opcao:
            case "1": Shape.listar_todos_comprimentos()
            case "2": Shape.listar_areas_totais()
        
    else:
        print("Opção inválida. Digite apenas 1 ou 2.")



if __name__ == "__main__":
    system("cls")
    main()

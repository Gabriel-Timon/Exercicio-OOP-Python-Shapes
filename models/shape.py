from abc import ABC, abstractmethod

class Shape(ABC):
    lista_shapes = list()

    @abstractmethod
    def area(self):
        pass

    
    @abstractmethod
    def comprimento(self):
        pass

    
    @classmethod
    def listar_areas_totais(cls):
        print("TODAS AS ÁREAS")
        print('-' * 20)
        for i, shape in enumerate(cls.lista_shapes):
            print(f"--- SHAPE {i+1} ---")
            print(f"Shape: {shape._shape}\nÁrea: {shape.area()} cm²\n")

    @classmethod
    def listar_todos_comprimentos(cls):
        print("TODOS OS COMPRIMENTOS")
        print('-' * 20)
        for i, shape in enumerate(cls.lista_shapes):
            print(f"--- SHAPE {i+1} ---")
            print(f"Shape: {shape._shape}\nComprimento: {shape.comprimento()} cm\n")

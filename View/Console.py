import sys

from Entities.Board import Board


class Console:
    def __init__(self):
        self.SCRIPT = '-'
        self.option: int = None

    def mainMenu(self):
        while True:
            print(self.SCRIPT * 30)
            print("Bienvenido al juego NIM")
            print(self.SCRIPT * 30)
            print("Seleccione una opcion: ")
            print("1. Iniciar juego")
            print("2. Salir")
            self.option = int(input("Ingrese su opcion: "))
            if self.option == 1:
                stack = int(input("Ingrese la cantidad de pilas: "))
                objectsinstack = []
                for i in range(stack):
                    objectinstack = int(input("Ingrese la cantidad de objetos de cada stack: "))
                    objectsinstack.append(objectinstack)
                board = Board()
                board.construct(stack, objectsinstack)

            elif self.option == 2:
                sys.exit()
            else:
                print("Ingrese una opción válida")

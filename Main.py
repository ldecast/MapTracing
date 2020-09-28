import Automata

class Main:
    from os import system
    def __init__(self):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                   MapTracing                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        self.inicio(opcion)
    
    def inicio(self,opcion):
        #fichero = input("Ingrese la ruta del archivo '.txt'----> ")
        fichero = "C:\\Users\\luisd\\Desktop\\hola.txt"
        if opcion=="1":
            # print("\n")
            Automata.Automata().aceptar(fichero)
        elif opcion=="2":
            print("\n")
            eInicio = input("Estación inicio: ")
            eFinal = input("Estación final: ")
            
        elif opcion=="3":
            print("\n")
            
            
        elif opcion=="4":
            self.system('cls')
            print("\nSaliendo...")
            exit()
        else:
            opcion = input("Seleccione una opción valida [1-4]: ")
            self.inicio(opcion)
        
run=Main()
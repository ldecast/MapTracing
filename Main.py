import Automata
class Main:
    from os import system
    def __init__(self, init):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                   MapTracing                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa")
        print("4. Salir")
        opcion = input("\nIngrese una opción: ")
        self.inicio(opcion,init)
    
    def inicio(self,opcion,init):
        #fichero = input("Ingrese la ruta del archivo '.txt'----> ")
        fichero = "C:\\Users\\luisd\\Desktop\\hola.txt"
        if opcion=="1":
            print("\nLeyendo: ---"+fichero+"---\n")
            aceptacion = Automata.Automata().aceptar(fichero, None, None)
            if aceptacion == False:
                print("El archivo seleccionado no se encuentra. Intente de nuevo.")
                input("Presione Enter para continuar...")
                Main(None)
            else:
                input("Presione Enter para continuar...")
                Main(aceptacion)

        elif opcion=="2":
            if init == None:
                print("No se ha leído ningún archivo.")
                input("Presione Enter para continuar e ingrese una entrada: ")
                Main(None)
            else:
                print("\n")
                eInicio = input("Estación inicio: ")
                eFinal = input("Estación final: ")
                Automata.Automata().aceptar(init,eInicio,eFinal)
                
            
        elif opcion=="3":
            print("\n")
            
            
        elif opcion=="4":
            self.system('cls')
            print("\nSaliendo...")
            exit()
        else:
            opcion = input("Seleccione una opción valida [1-4]: ")
            self.inicio(opcion,init)
        
run=Main(None)
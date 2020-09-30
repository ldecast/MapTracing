import Automata
class Main:
    from os import system
    def __init__(self, init, inicio, fin):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                   MapTracing                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa")
        print("4. Salir")
        opcion = input("\nIngrese una opción: ")
        self.inicio(opcion,init,inicio,fin)
    
    def inicio(self,opcion,init,inicio,fin):
        #fichero = input("Ingrese la ruta del archivo '.txt'----> ")
        fichero = "C:\\Users\\luisd\\Desktop\\archivo.txt"
        if opcion=="1":
            print("\nLeyendo: ---"+fichero+"---\n")
            aceptacion = Automata.Automata().aceptar(fichero, None, None, 0)
            if aceptacion == False:
                print("El archivo seleccionado no se encuentra. Intente de nuevo.")
                input("Presione Enter para continuar...")
                Main(None,None,None)
            else:
                input("Presione Enter para continuar...")
                Main(aceptacion,None,None)

        elif opcion=="2":
            if init == None:
                print("No se ha leído ningún archivo.")
                input("Presione Enter para continuar e ingrese una entrada: ")
                Main(None,None,None)
            else:
                print("\n")
                eInicio = input("Estación inicio: ")
                eFinal = input("Estación final: ")
                print("\nGenerando ruta de "+eInicio+" a "+eFinal+"...")
                # Automata.Automata().aceptar(init,eInicio,eFinal,2)
                input("Presione Enter para continuar...")
                Main(init,eInicio,eFinal)
                
            
        elif opcion=="3":
            if init == None:
                print("No se ha leído ningún archivo.")
                input("Presione Enter para continuar e ingrese una entrada: ")
                Main(None,None,None)
            elif inicio == None or fin == None:
                print("No se ha ingresado ninguna estación de inicio o de fin.")
                input("Presione Enter para continuar e ingrese dos estaciones: ")
                Main(init,None,None)
            elif init != None and inicio != None and fin != None:
                print("\nGenerando mapa...")
                Automata.Automata().aceptar(init,inicio,fin,3)
                input("Presione Enter para continuar...")
                Main(init,None,None)
            
            
        elif opcion=="4":
            self.system('cls')
            print("\nSaliendo...")
            exit()
        else:
            opcion = input("Seleccione una opción valida [1-4]: ")
            self.inicio(opcion,init,inicio,fin)
        
run=Main(None,None,None)
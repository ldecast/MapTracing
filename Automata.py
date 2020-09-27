import Estacion
import Ruta
class Automata:

    def aceptar(self, entrada):
        file = open(entrada, 'r', encoding= "utf8") 
        # file = open("C:\\Users\\luisd\\Desktop\\hola.txt",'r',encoding="utf8")
        fila = 1
        columna = 0
        lexema = ""
        estado = 0
        padre = []
        # tipoPadre = ""

        for linea in file.readlines():
            for caracter in linea:
                columna += 1
                if caracter == "\n" or caracter == "\r":
                    fila += 1
                    columna = 1
                    continue
                elif caracter == "\t":
                    # columna += 4
                    continue
                elif caracter == " ":
                    # columna +=1
                    continue
                elif estado == -1:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 1
                    continue
                elif estado == -2:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 2
                    continue
                # elif estado == -3:
                #     print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                #     estado = 3
                #     continue
                elif estado == -4:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 4
                    continue
                elif estado == -5:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 5
                    continue
                elif estado == -6:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 6
                    continue
                elif estado == -7:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 7
                    continue
                elif estado == -8:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 8
                    continue
                elif estado == -9:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 9
                    continue
                elif estado == -10:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 10
                    continue
                elif estado == -11:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 11
                    continue
                elif estado == -12:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 12
                    continue
                elif estado == -13:
                    print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                    estado = 0
                    continue


                lexema = lexema + caracter

                if estado == 0:
                    if caracter == "<":
                        estado = 1
                    # elif ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                    #     estado = 4
                    # elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                    #     estado = 5
                    # elif caracter == '#':
                    #     estado = 7
                    else:
                        estado = -13
                
                elif estado == 1:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 2
                    elif caracter == "/":
                        estado = 10
                    else:
                        estado = -1
                    
                elif estado == 2:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 2
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 2
                    elif caracter == '_':
                        estado = 2
                    elif caracter == ">":
                        estado = 3
                    else:
                        estado = -2
                    
                elif estado == 3:
                    # padre.append(lexema)
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 4
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 5
                    elif caracter == '#':
                        estado = 7
                    elif caracter == "<":
                        estado = 1
                    else:
                        print("Fila: "+str(fila) + "Columna: " + str(columna) + "Caracter: " + caracter)
                        estado = 3
                        continue
                        # estado = -3

                elif estado == 4:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 4
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 4
                    elif caracter == '_':
                        estado = 4
                    elif caracter == "<":
                        estado = 9
                    else:
                        estado = -4
                
                elif estado == 5:
                    if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 5
                    elif caracter == ".":
                        estado = 6
                    elif caracter == "<":
                        estado = 9
                    else:
                        estado = -5
                
                elif estado == 6:
                    if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 6
                    elif caracter == "<":
                        estado = 9
                    else:
                        estado = -6
                
                elif estado == 7:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 8
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 8
                    else:
                        estado = -7
                
                elif estado == 8:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 8
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 8
                    elif caracter == "<":
                        estado = 9
                    else:
                        estado = -8
                
                elif estado == 9:
                    
                    if caracter == "/":
                        estado = 10
                    else:
                        estado = -9

                elif estado == 10:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 11
                    else:
                        estado = -10

                elif estado == 11:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 11
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 11
                    elif caracter == '_':
                        estado = 11
                    elif caracter == ">":
                        estado = 12
                    else:
                        estado = -11
                
                elif estado == 12:
                    if caracter == "<":
                        estado = 9
                    else:
                        estado == -12

                
            if estado == 12:# or estado == 3 or estado == 4 or estado == 5 or estado == 7: #saber si la cadena es valida
                # if estado == 12:
                print("CADENA ACEPTADA: " +lexema)
                print('')
                estado = 0
                lexema = ''
                
            elif estado == 0 or estado == 4 or estado == 3:
                continue

            # elif estado == -1:
                
            else:
                print('Cadena inválida: '+lexema+'\n'+"Estado: "+str(estado))

            # estado = 0
            # lexema = ''
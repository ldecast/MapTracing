import Estacion
import Ruta
import Graficador
class Automata:

    def aceptar(self, entrada):
        file = open(entrada, 'r', encoding= "utf8") 
        # file = open("C:\\Users\\luisd\\Desktop\\hola.txt",'r',encoding="utf8")
        fila = 1
        columna = 0
        lexema = ""
        estado = 0
        padre = []
        errores = 0
        error_lista = []
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
                        errores +=1
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        # Graficador.Graficador().reportar(errores,fila,columna,caracter,"Desconocido")
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 0
                        continue
                
                elif estado == 1:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 2
                    elif caracter == "/":
                        estado = 10
                    else:
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        print("Fila: "+str(fila) + " Columna: " + str(columna) + " Caracter: " + caracter)
                        estado = 1
                        continue
                    
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
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 2
                        continue
                    
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
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
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
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 4
                        continue
                
                elif estado == 5:
                    if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 5
                    elif caracter == ".":
                        estado = 6
                    elif caracter == "<":
                        estado = 9
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 5
                        continue
                
                elif estado == 6:
                    if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 6
                    elif caracter == "<":
                        estado = 9
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 6
                        continue
                
                elif estado == 7:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 8
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 8
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 7
                        continue
                
                elif estado == 8:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 8
                    elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                        estado = 8
                    elif caracter == "<":
                        estado = 9
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        estado = 8
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        continue
                
                elif estado == 9:
                    if caracter == "/":
                        estado = 10
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        estado = 9
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        continue

                elif estado == 10:
                    if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                        estado = 11
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        estado = 10
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        continue            

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
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 11
                        continue 
                
                elif estado == 12:
                    if caracter == "<":
                        estado = 9
                    else:
                        print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                        errores +=1
                        error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                        estado = 12
                        continue 

                
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
        if not error_lista == []:
            Graficador.Graficador().reportar(error_lista)
            # estado = 0
            # lexema = ''
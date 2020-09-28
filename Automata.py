import Estacion
import Ruta
import Graficador
class Automata:

    def token(self, lexema):
        a = lexema.lower()
        if 'ruta' in a:
            return 'ruta'
        elif 'estacion' in a:
            return 'estación'
        elif 'nombre' in a:
            return 'nombre'
        elif 'peso' in a:
            return 'peso'
        elif 'inicio' in a:
            return 'inicio'
        elif 'fin' in a:
            return 'fin'
        elif 'estado' in a:
            return 'estado'
        elif 'color' in a:
            return 'color'
    
    def get_lexema(self, lexema):
        if lexema.count('>') > 1:
            a = [idx for idx, x in enumerate(lexema) if x=='<']
            b = [idx for idx, x in enumerate(lexema) if x=='>']
            c = lexema[a.pop()+1:b.pop()]
            return c
        elif lexema.count('>') == 1:
            a = lexema[lexema.index('<')+1:lexema.index('>')]
            return a


    def aceptar(self, entrada, estacion_inicio, estacion_final):
        
        try:
            file = open(entrada, 'r', encoding= "utf8") 
            fila = 0
            columna = 0
            lexema = ""
            estado = 0
            tokens = 0
            token_lista = []
            errores = 0
            error_lista = []
            # tipoPadre = ""

            for linea in file.readlines():
                fila = fila + 1
                columna = 0
                for caracter in linea:
                    columna = columna + 1
                    if caracter == "\n": #or caracter == "\r":
                        continue
                    elif caracter == "\t":
                        continue
                    elif caracter == " ":
                        continue


                    lexema = lexema + caracter

                    if estado == 0:
                        if caracter == "<":
                            estado = 1
                        else:
                            errores +=1
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            # print(lexema, fila, columna)
                            tokens += 1
                            token_lista.append([tokens, self.get_lexema(lexema), fila, columna, self.token(self.get_lexema(lexema))])
                            estado = 3
                        else:
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 2
                            continue
                        
                    elif estado == 3:
                        # print(lexema, fila, columna)
                        # tokens += 1
                        # token_lista.append([tokens, self.lexem(lexema), fila, columna, self.token(self.lexem(lexema))])
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 4
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 5
                        elif caracter == '#':
                            estado = 7
                        elif caracter == "<":
                            estado = 1
                        else:
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            estado = 8
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            continue
                    
                    elif estado == 9:
                        if caracter == "/":
                            estado = 10
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            estado = 9
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            continue

                    elif estado == 10:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
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
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 11
                            continue 
                    
                    elif estado == 12:
                        if caracter == "<":
                            estado = 9
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 12
                            continue 

                    
                if estado == 12:# or estado == 3 or estado == 4 or estado == 5 or estado == 7: #saber si la cadena es valida
                    # if estado == 12:
                    # print("CADENA ACEPTADA: " +lexema)
                    # print('')
                    estado = 0
                    lexema = ''
                    
                elif estado == 0 or estado == 4 or estado == 3:
                    # if estado == 3:
                        # print(lexema)
                        # tokens += 1
                        # token_lista.append([tokens, self.lexem(lexema), fila, columna, self.token(self.lexem(lexema))])
                    continue

                # elif estado == -1:
                    
                else:
                    print('Cadena inválida: '+lexema+'\n'+"Estado: "+str(estado))

            if not error_lista == [] and estacion_inicio == None and estacion_final == None:
                Graficador.Graficador().reportar(error_lista)
            if not token_lista == [] and estacion_inicio == None and estacion_final == None:
                Graficador.Graficador().tokens(token_lista)
            
            # if estacion_inicio != None:
            #     estacion_inicio
            
            return entrada

        except FileNotFoundError:
            return False
        
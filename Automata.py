import Reportador
import Graficador

class Automata:

    def token(self, lexema):
        a = lexema.lower()
        if 'ruta' in a:
            return 'ruta'
        elif 'estacion' in a:
            return 'estacion'
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


    def aceptar(self, entrada, estacion_inicio, estacion_final, opcion):
        
        try:
            file = open(entrada, 'r', encoding= "utf-8-sig") 
            fila = 0
            columna = 0
            aux_col = 0
            nombre = ""
            lexema = ""
            estado = 0
            tokens = 0
            token_lista = []
            errores = 0
            error_lista = []
            rutas = []
            estaciones = []

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
                        elif caracter == "":
                            continue
                        else:
                            errores +=1
                            # print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 0
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 1:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            aux_col = columna
                            estado = 2
                        elif caracter == "/":
                            estado = 10
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            # print("Fila: "+str(fila) + " Columna: " + str(columna) + " Caracter: " + caracter)
                            estado = 1
                            lexema = lexema.replace(caracter,'')
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
                            token_lista.append([tokens, self.get_lexema(lexema), fila, aux_col, self.token(self.get_lexema(lexema))])
                            estado = 3
                        else:
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 2
                            lexema = lexema.replace(caracter,'')
                            continue
                        
                    elif estado == 3:
                        # print(lexema)
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
                            # print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 3
                            lexema = lexema.replace(caracter,'')
                            continue
                            # estado = -3

                    elif estado == 4:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 4
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 4
                        elif caracter == '_':
                            estado = 4
                        elif caracter == '@':
                            estado = 4
                        elif caracter == '#':
                            estado = 4
                        elif caracter == "<":
                            estado = 9
                        else:
                            ###print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 4
                            lexema = lexema.replace(caracter,'')
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
                            lexema = lexema.replace(caracter,'')
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
                            lexema = lexema.replace(caracter,'')
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
                            lexema = lexema.replace(caracter,'')
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
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 9:
                        if caracter == "/":
                            estado = 10
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            estado = 9
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue

                    elif estado == 10:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            estado = 10
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue            

                    elif estado == 11:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 11
                        elif caracter == '_':
                            estado = 11
                        elif caracter == ">":
                            # print(lexema)
                            
                            estado = 12
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 11
                            lexema = lexema.replace(caracter,'')
                            continue 
                    
                    elif estado == 12:
                        
                        if caracter == "<":
                            estado = 1
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 12
                            lexema = lexema.replace(caracter,'')
                            continue 

                    
                if estado == 12:# or estado == 3 or estado == 4 or estado == 5 or estado == 7: #saber si la cadena es valida
                    print("CADENA ACEPTADA: " +lexema)
                    a = lexema.lower()
                    count = 0
                    count2 = 0
                    if a.count('<')>1 and 'ruta' in a or 'peso' in a or 'inicio' in a or 'fin' in a:
                        count += 1
                        rutas.append(lexema)
                    if a.count('<')>1 and 'estacion' in a and 'nombre' in a or 'estado' in a or 'color' in a:
                        estaciones.append(lexema)
                        count2 += 1
                    if a.count('<')>1 and 'nombre' in a and not 'estacion' in a:
                        nombre = lexema
                    # print('')
                    estado = 0
                    lexema = ''
                    # print(rutas)
                    
                elif estado == 0 or estado == 4 or estado == 3 or estado == 6 or estado == 8:
                    
                    continue

                # elif estado == -1:
                    
                else:
                    print('Cadena inválida: '+lexema+'\n'+"Estado: "+str(estado))



            if error_lista != [] and estacion_inicio == None and estacion_final == None:
                Reportador.Reportador().error(error_lista)
            if token_lista != [] and estacion_inicio == None and estacion_final == None:
                Reportador.Reportador().tokens(token_lista)
            
            

            if estacion_inicio != None and estacion_final != None:
                if opcion == 2:
                    Graficador.Graficador().graficar_ruta(rutas,estaciones,estacion_inicio,estacion_final)
                elif opcion == 3:
                    Graficador.Graficador().graficar_mapa(rutas,estaciones,estacion_inicio,estacion_final,nombre)
            

            file.close()
            return entrada

        except FileNotFoundError:
            return False
        
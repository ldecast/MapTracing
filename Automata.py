import Estacion
import Ruta
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
    
    def get_estacion(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if 'estacion' in lista[indice].lower() and 'nombre' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    def get_estado(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if 'estado' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    def get_color(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if 'color' in lista[indice]:
                    f = lista[indice]
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    
    def get_ruta(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 5:
                a += 1
                if 'ruta' in lista[indice].lower() and 'nombre' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    
    def get_peso(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 5:
                a += 1
                if 'peso' in lista[indice].lower():
                    f = lista[indice]
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None

    def get_inicio(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 5:
                a += 1
                if 'inicio' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None

    def get_fin(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 5:
                a += 1
                if 'fin' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    
    def get_lexema(self, lexema):
        if lexema.count('>') > 1:
            a = [idx for idx, x in enumerate(lexema) if x=='<']
            b = [idx for idx, x in enumerate(lexema) if x=='>']
            c = lexema[a.pop()+1:b.pop()]
            return c
        elif lexema.count('>') == 1:
            a = lexema[lexema.index('<')+1:lexema.index('>')]
            return a

    def get_padre(self, lexema):
        # print(lexema)
        if lexema.count('>') == 3:
            a = [idx for idx, x in enumerate(lexema) if x=='>']
            b = [idx for idx, x in enumerate(lexema) if x=='<']
            c = lexema[a.pop(1)+1:b.pop(2)]
            return c
        if lexema.count('>') == 2:
            a = [idx for idx, x in enumerate(lexema) if x=='>']
            b = [idx for idx, x in enumerate(lexema) if x=='<']
            c = lexema[a.pop(0)+1:b.pop(1)]
            return c
        # elif lexema.count('>') == 1:
            # a = lexema[lexema.index('<')+1:lexema.index('>')]
            

    def aceptar(self, entrada, estacion_inicio, estacion_final):
        
        try:
            file = open(entrada, 'r', encoding= "utf8") 
            fila = 0
            columna = 0
            aux_col = 0
            lexema = ""
            estado = 0
            tokens = 0
            token_lista = []
            errores = 0
            error_lista = []
            # tipoPadre = ""
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
                        else:
                            errores +=1
                            # print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 0
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
                            # print(lexema)
                            
                            estado = 12
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 11
                            continue 
                    
                    elif estado == 12:
                        
                        if caracter == "<":
                            estado = 1
                        else:
                            ##print("Fila: "+str(fila) + " Columna: " + str(columna) +  " Caracter: " + caracter)
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 12
                            continue 

                    
                if estado == 12:# or estado == 3 or estado == 4 or estado == 5 or estado == 7: #saber si la cadena es valida
                    # if estado == 12:
                    print("CADENA ACEPTADA: " +lexema)
                    a = lexema.lower()
                    count = 0
                    count2 = 0
                    nombre_ruta = ''
                    peso = ''
                    inicio = ''
                    fin = ''
                    nombre_estacion = ''
                    estado_estacion = ''
                    color = ''
                    # if 'ruta' in lexema and 'nombre' in a:
                    #     nombre_ruta = lexema
                    # elif 'peso' in a:
                    #     peso = lexema
                    # elif 'inicio' in a:
                    #     inicio = lexema
                    # elif 'fin' in a:
                    #     fin = lexema
                    # elif 'estacion' in a and 'nombre' in a:
                    #     nombre_estacion = lexema
                    # elif 'estado' in a:
                    #     estado_estacion = lexema
                    # elif 'color' in a:
                    #     color = lexema
                    if a.count('<')>1 and 'ruta' in a or 'peso' in a or 'inicio' in a or 'fin' in a:
                        count += 1
                        rutas.append(lexema)
                    if a.count('<')>1 and 'estacion' in a and 'nombre' in a or 'estado' in a or 'color' in a:
                        estaciones.append(lexema)
                        count2 += 1
                    # print('')
                    estado = 0
                    lexema = ''
                    # print(rutas)
                    
                elif estado == 0 or estado == 4 or estado == 3 or estado == 6 or estado == 8:
                    # if estado == 3:
                        # print(lexema)
                        # tokens += 1
                        # token_lista.append([tokens, self.lexem(lexema), fila, columna, self.token(self.lexem(lexema))])
                    continue

                # elif estado == -1:
                    
                else:
                    print('Cadena inválida: '+lexema+'\n'+"Estado: "+str(estado))

            # if error_lista != [] and estacion_inicio == None and estacion_final == None:
            #     Graficador.Graficador().reportar(error_lista)
            # if token_lista != [] and estacion_inicio == None and estacion_final == None:
            #     Graficador.Graficador().tokens(token_lista)
            
            # lista_rutas = rutas
            # lista_estaciones = estaciones
            # print(rutas)
            # print(estaciones)

            if estacion_inicio != None and estacion_final != None:
                Graficador.Graficador().graficar_ruta(rutas,estaciones,estacion_inicio, estacion_final)
                Graficador.Graficador().graficar_mapa(rutas,estaciones,estacion_inicio, estacion_final)
            
            return entrada

        except FileNotFoundError:
            return False
        
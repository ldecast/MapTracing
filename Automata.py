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
            aux_lex = []
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
                    if caracter == "\n":
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
                            estado = 1
                            lexema = lexema.replace(caracter,'')
                            continue
                        
                    elif estado == 2:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 2
                        elif caracter == ">":
                            tokens += 1
                            token_lista.append([tokens, self.get_lexema(lexema), fila, aux_col, self.token(self.get_lexema(lexema))])
                            estado = 3
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 2
                            lexema = lexema.replace(caracter,'')
                            continue
                        
                    elif estado == 3:                        
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 4
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 5
                        elif caracter == '#':
                            estado = 7
                        elif caracter == "<":
                            estado = 1
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 3
                            lexema = lexema.replace(caracter,'')
                            continue

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
                            errores +=1
                            estado = 8
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 9:
                        if caracter == "/":
                            estado = 10
                        else:
                            errores +=1
                            estado = 9
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue

                    elif estado == 10:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                        else:
                            errores +=1
                            estado = 10
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue            

                    elif estado == 11:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                        elif caracter == ">":
                            estado = 12
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 11
                            lexema = lexema.replace(caracter,'')
                            continue 
                    
                    if estado == 12:
                        # print("CADENA ACEPTADA: " +lexema)
                        aux_lex.append(lexema.lower())
                        estado = 0
                        lexema = ''

                else:
                    continue


            if error_lista != [] and opcion == '1':
                Reportador.Reportador().error(error_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            if token_lista != [] and opcion == '1':
                Reportador.Reportador().tokens(token_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            
            for j in range(len(aux_lex)):
                try:
                    if '<nombre>' in aux_lex[j] and not '<ruta>' in aux_lex[j] and not '<estacion>' in aux_lex[j]:
                        if '/estacion' in aux_lex[j-1] or '/ruta' in aux_lex[j-1]:
                            nombre = aux_lex[j]
                    if '<nombre>' in aux_lex[j] and not '<estacion>' in aux_lex[j] and not '<ruta>' in aux_lex[j]:
                        if '<estacion>' in aux_lex[j-1] or '</estacion>' in aux_lex[j+1]:
                            estaciones.append(aux_lex[j])
                        else:
                            rutas.append(aux_lex[j])
                    if '<estacion>' in aux_lex[j] or '<estado>' in aux_lex[j] or '<color>' in aux_lex[j]:
                        if not '<ruta>' in aux_lex[j-1] and not '</ruta>' in aux_lex[j+1]:
                            estaciones.append(aux_lex[j])
                    if '<ruta>' in aux_lex[j] or '<peso>' in aux_lex[j] or '<inicio>' in aux_lex[j] or '<fin>' in aux_lex[j]:
                        if not '<estacion>' in aux_lex[j-1] and not '</estacion>' in aux_lex[j+1]:
                            rutas.append(aux_lex[j])
                    
                except IndexError:
                    pass
            
            try:
                if nombre != "":                  
                    try:
                        rutas.remove(nombre)
                        estaciones.remove(nombre)
                    except ValueError:
                        estaciones.remove(nombre)
                        rutas.remove(nombre)
            except ValueError:
                pass

            if estacion_inicio != None and estacion_final != None:
                if opcion == '2' or opcion == '5':
                    Graficador.Graficador().graficar_ruta(rutas,estaciones,estacion_inicio,estacion_final,opcion)
                elif opcion == '3':
                    Graficador.Graficador().graficar_mapa(rutas,estaciones,estacion_inicio,estacion_final,nombre)
            
            if opcion == '6':
                Graficador.Graficador().mapa_sin_traza(rutas,estaciones,nombre)
            
            file.close()
            return entrada

        except FileNotFoundError:
            return False
import os
class Graficador:

    def get_estacion(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if '<nombre>' in lista[indice].lower() and not '<ruta>' in lista[indice].lower():
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
                if '<estado>' in lista[indice].lower():
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
                if '<color>' in lista[indice]:
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
                if '<nombre>' in lista[indice].lower():
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
                if '<peso>' in lista[indice].lower():
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
                if '<inicio>' in lista[indice].lower():
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
                if '<fin>' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None
    
    def limpiar(self, lexema):
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
        
    def purificar(self, lexema, tipo):
        if tipo == "estacion" or tipo == "inicio" or tipo == "fin":
            f = lexema
            while(not f[0].isalpha()):
               f = f[1:]
            while(f[-1] != "_" and not f[-1].isalnum()):
               f = f[:-1]
            return 'ESTACION'+f

        elif tipo == "ruta":
            f = lexema
            while(not f[0].isalpha()):
                f = f[1:]
            while(f[-1] != "_" and not f[-1].isalnum()):
                f = f[:-1]
            return 'RUTA'+f

        elif tipo == "estado":
            f = lexema
            while(f[0] != "d" and f[0] != "c"):
               f = f[1:]
            while(f[-1] != "e" and f[-1] != "a"):
               f = f[:-1]
            return 'ESTADO'+f

        elif tipo == "color":
            f = lexema
            while(f[0] != "#"):
               f = f[1:]
            while(not f[-1].isalnum()):
               f = f[:-1]
            return 'COLOR'+f

        
        elif tipo == "peso":
            f = lexema
            while(not f[0].isnumeric()):
               f = f[1:]
            while(not f[-1].isnumeric()):
               f = f[:-1]
            return 'PESO'+f
            
    
    def graficar_ruta(self, lista_rutas, lista_estaciones, eInicio, eFin, opcion):
        node = ''
        contenido = ''

        estacion = []
        d = 0
        for x in range(len(lista_estaciones)):
            a = self.get_estacion(lista_estaciones,d)
            b = self.get_estado(lista_estaciones,d)
            c = self.get_color(lista_estaciones,d)
            d += 3
            if a!=None and b!=None and c!=None:
                if len(a)>3 and len(b)>3 and len(c)>3:
                    estacion.append([self.purificar(self.limpiar(a),"estacion"),self.purificar(self.limpiar(b),"estado"),self.purificar(self.limpiar(c),"color")])

        ruta = []
        e = 0
        for y in range(len(lista_rutas)):
            a = self.get_ruta(lista_rutas,e)
            b = self.get_peso(lista_rutas,e)
            c = self.get_inicio(lista_rutas,e)
            d = self.get_fin(lista_rutas,e)
            e += 4
            if a!=None and b!=None and c!=None and d!=None:
                if len(a)>3 and len(b)>3 and len(c)>3 and len(d)>3:
                    ruta.append([self.purificar(self.limpiar(a),"ruta"),self.purificar(self.limpiar(b),"peso"),self.purificar(self.limpiar(c),"inicio"),self.purificar(self.limpiar(d),"fin")])

        match1 = ''
        match2 = ''

        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eInicio == estacion[i][j].replace('ESTACION',''):
                    match1 = estacion[i][j].replace('ESTACION','')
        
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eFin == estacion[i][j].replace('ESTACION',''):
                    match2 = estacion[i][j].replace('ESTACION','')
        

        if match1 != match2 and match1 != '' and match2 != '':

            directorio = str("Ruta [" + eInicio + "-" + eFin + "]")+'.dot'
            grafo = open(directorio,'w',encoding="utf8")
            grafo.write('digraph D {\n')
            grafo.write("rankdir=\"LR\";\n")
            grafo.write("splines=false;\n")
            grafo.write("bgcolor=\"#abb2b9\";\n")
            grafo.write("node[shape = \"ellipse\" style=filled fontname = \"Century Gothic\" color= \"#283747\"];\n")
            grafo.write("edge[arrowhead=vee color=\"#566573\" fontname=\"Sans-Serif\" fontsize=\"10\" penwidth=\"0.35\"];\n")
            for i in range(len(estacion)):
                for j in range(len(estacion[i])):
                    if 'ESTACION' in estacion[i][j] and contenido == '':
                        node = estacion[i][j].replace('ESTACION','')
                        contenido = str(node) + '[label = \"'+estacion[i][j].replace('ESTACION','')
                    elif 'ESTADO' in estacion[i][j]:
                        contenido = contenido + "\\n"+estacion[i][j].replace('ESTADO','')+"\""
                    elif 'COLOR' in estacion[i][j] and contenido != '':
                        contenido = contenido + "  fillcolor=\""+ estacion[i][j].replace('COLOR','') +"\"];\n"
                grafo.write(contenido)
                contenido = ''
            recorrido = ''
            flecha = ''
            peso = ''
            for k in range(len(ruta)):
                for l in range(len(ruta[k])):
                    if 'RUTA' in ruta[k][l]:
                        flecha = ruta[k][l].replace('RUTA','')
                    if 'PESO' in ruta[k][l] or ruta[k][l].isdigit():
                        peso = ruta[k][l].replace('PESO','')
                    if 'ESTACION' in ruta[k][l] and recorrido != '':
                        recorrido = recorrido + "->" + ruta[k][l].replace('ESTACION','')
                    if 'ESTACION' in ruta[k][l] and recorrido=='':
                        recorrido = ruta[k][l].replace('ESTACION','')
                recorrido = recorrido + "[label = \""+ flecha + "\\n" + peso +"\"]\n"
                grafo.write(recorrido)
                recorrido = ''

            grafo.write('}')
            grafo.close()

            if self.ruta_rapida(match1,match1,match2,directorio) != False and opcion == '2':
                self.revisar(directorio)
            
                pre = directorio[:directorio.index('.dot')]
                os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
                os.startfile('\"'+pre+'.pdf\"')
                input("Ruta generada! Presione Enter para continuar...")

            elif opcion == '5':
                pre = directorio[:directorio.index('.dot')]
                os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
                os.startfile('\"'+pre+'.pdf\"')
                input("Ruta generada! Presione Enter para continuar...")


        else:
            print("No se ha podido reconocer una estación válida. Por favor intente de nuevo.")
            input("Presione Enter para continuar...")

    def graficar_mapa(self, lista_rutas, lista_estaciones, eInicio, eFin, name):
        titulo = ''
        if name != '' and name != None:
            titulo = self.limpiar(name).capitalize()

        node = ''
        contenido = ''

        estacion = []
        d = 0
        for x in range(len(lista_estaciones)):
            a = self.get_estacion(lista_estaciones,d)
            b = self.get_estado(lista_estaciones,d)
            c = self.get_color(lista_estaciones,d)
            d += 3
            if a!=None and b!=None and c!=None:
                estacion.append([self.purificar(self.limpiar(a),"estacion"),self.purificar(self.limpiar(b),"estado"),self.purificar(self.limpiar(c),"color")])

        ruta = []
        e = 0
        for y in range(len(lista_rutas)):
            a = self.get_ruta(lista_rutas,e)
            b = self.get_peso(lista_rutas,e)
            c = self.get_inicio(lista_rutas,e)
            d = self.get_fin(lista_rutas,e)
            e += 4
            if a!=None and b!=None and c!=None and d!=None:
                ruta.append([self.purificar(self.limpiar(a),"ruta"),self.purificar(self.limpiar(b),"peso"),self.purificar(self.limpiar(c),"inicio"),self.purificar(self.limpiar(d),"fin")])

        match1 = ''
        match2 = ''

        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eInicio == estacion[i][j].replace('ESTACION',''):
                    match1 = estacion[i][j].replace('ESTACION','')
        
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eFin == estacion[i][j].replace('ESTACION',''):
                    match2 = estacion[i][j].replace('ESTACION','')


        if match1 != "" and match2 != "":

            directorio = str("Mapa [" + eInicio + "-" + eFin + "]")+'.dot'
            grafo = open(directorio,'w',encoding="utf8")
            grafo.write('digraph D {\n')
            grafo.write("rankdir=\"LR\";\n")
            grafo.write("splines=false;\n")
            grafo.write("bgcolor=\"#abb2b9\";\n")
            grafo.write("label=\"" + titulo + "\" fontname=\"Century Gothic\" labelloc=\"t\";\n")
            grafo.write("node[shape = \"ellipse\" style=filled fontname = \"Century Gothic\" color= \"#283747\"];\n")
            grafo.write("edge[arrowhead=vee color=\"#566573\" fontname=\"Sans-Serif\" fontsize=\"10\" penwidth=\"0.35\"];\n")
            for i in range(len(estacion)):
                for j in range(len(estacion[i])):
                    if 'ESTACION' in estacion[i][j] and contenido == '':
                        node = estacion[i][j].replace('ESTACION','')
                        contenido = str(node) + '[label = \"'+estacion[i][j].replace('ESTACION','')
                    elif 'ESTADO' in estacion[i][j] and contenido != '':
                        contenido = contenido + "\\n"+estacion[i][j].replace('ESTADO','')+"\""
                    elif 'COLOR' in estacion[i][j] and contenido != '':
                        contenido = contenido + "  fillcolor=\""+ estacion[i][j].replace('COLOR','') +"\"];\n"
                grafo.write(contenido)
                
                contenido = ''
            
            recorrido = ''
            flecha = ''
            peso = ''
            for k in range(len(ruta)):
                for l in range(len(ruta[k])):
                    if 'RUTA' in ruta[k][l]:
                        flecha = ruta[k][l].replace('RUTA','')
                    if 'PESO' in ruta[k][l] or ruta[k][l].isdigit():
                        peso = ruta[k][l].replace('PESO','')
                    if 'ESTACION' in ruta[k][l] and recorrido != '':
                        recorrido = recorrido + "->" + ruta[k][l].replace('ESTACION','')
                    if 'ESTACION' in ruta[k][l] and recorrido=='':
                        recorrido = ruta[k][l].replace('ESTACION','')
                recorrido = recorrido + "[label = \""+ flecha + "\\n" + peso +"\"]\n"
                grafo.write(recorrido)
                recorrido = ''

            grafo.write('}')
            grafo.close()

            if self.ruta_rapida(match1,match1,match2,directorio) != False:
                pre = directorio[:directorio.index('.dot')]
                os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
                os.startfile('\"'+pre+'.pdf\"')
                input("Mapa generado! Presione Enter para continuar...")
            
        else:
            print("No se ha podido reconocer una estación válida. Por favor intente de nuevo.")
            input("Presione Enter para continuar...")
        
    
    def ruta_rapida(self,inicio, nuevo_inicio, fin, dot):
        done = False
        reader = open(dot,'r')
        rutas_posibles = []
        cerradas = []

        super_aux = []
        super_aux.append(str('->'+inicio))
        for linea in reader.readlines():
            if 'cerrad' in linea:
                cerradas.append(linea[:linea.index('[')])
            if nuevo_inicio == fin:
                done = True
                break
            elif str(nuevo_inicio+'->') in linea:
                    rutas_posibles.append(linea)

        for cerrado in cerradas:
            for posible in rutas_posibles:
                if cerrado in posible:
                    rutas_posibles.remove(posible)

        reader.close()
        if inicio in cerradas or fin in cerradas:
            input("Una de las estaciones que ingresó se encuentra fuera de servicio! Valide nuevamente.")
            done = True
            return False
        if done == False:
            self.evaluar(rutas_posibles,inicio,nuevo_inicio,fin,dot, super_aux)
                
        
    def evaluar(self,linea, inicio, nuevo_inicio, fin,dot, super_aux):
        nuevo_inicio = ''
        peso = []
        ruta_vieja = ''
        ruta_pintar = ''
        fast = ''
        for dato in linea:
            if str(nuevo_inicio+'->') in dato:
                peso.append(dato[dato.rfind('\\n')+2:dato.rfind('"')])
        if peso!= []:
            fast = min(peso)
            for dato in linea:
                if str(fast) == dato[dato.rfind('\\n')+2:dato.rfind('"')]:
                    nuevo_inicio = dato[dato.index('>')+1:dato.index('[')]
                    ruta_vieja = dato
                    ruta_pintar = dato.replace(']',' penwidth=\"2\" color=\"#196f3d\"]')
                    super_aux.append(str('->'+nuevo_inicio))
            self.ruta_rapida2(inicio,nuevo_inicio,fin,dot, super_aux)
            self.sobre_escribir(dot,ruta_vieja,ruta_pintar)
        else:
            return False

    def ruta_rapida2(self,inicio, nuevo_inicio, fin, dot, super_aux):
        done = False
        reader = open(dot,'r')
        rutas_posibles = []
        cerradas = []
        
        for linea in reader.readlines():
            if 'cerrad' in linea:
                cerradas.append(linea[:linea.index('[')])
            if nuevo_inicio == fin:
                done = True
                break
            elif str(nuevo_inicio+'->') in linea:
                if not linea[linea.index('>')-1:linea.index('[')] in super_aux:
                    rutas_posibles.append(linea)
                    if not str('->'+fin) in linea:
                        super_aux.append(str('->'+nuevo_inicio))
                        super_aux.append(linea[linea.index('>')-1:linea.index('[')])

        for cerrado in cerradas:
            for posible in rutas_posibles:
                if cerrado in posible:
                    rutas_posibles.remove(posible)

        reader.close()
        if done == False:
            try:
                self.evaluar(rutas_posibles,inicio,nuevo_inicio,fin,dot,super_aux)
            except RecursionError:
                print('...!')

    def sobre_escribir(self,dot,ruta_vieja,ruta_nueva):
        reader = open(dot,'r')
        lineas = []
        for linea in reader.readlines():
            if not ruta_vieja in linea:
                lineas.append(linea)
            if ruta_vieja in linea:
                lineas.append(ruta_vieja.replace(ruta_vieja,ruta_nueva))
        reader.close()

        writer = open(dot, 'w')
        for dato in lineas:
            writer.write(dato)
        writer.close()


    def revisar(self, directorio):
        reader = open(directorio,'r')
        lineas = []
        for linea in reader.readlines():
            if 'color=\"#196f3d\"' in linea:
                lineas.append(linea[:linea.index('-')])
                lineas.append(linea[linea.index('>')+1:linea.index('[')])
        reader.close()
        h = list(set(lineas))

        reader2 = open(directorio,'r')
        x = []
        for y in reader2.readlines():
            for new in h:
                if new in y and 'color=' in y:
                    x.append(y)
        reader2.close()
        z = list(set(x))

        grafo = open(directorio, 'w')
        grafo.write('digraph D {\n')
        grafo.write("rankdir=\"LR\";\n")
        grafo.write("splines=false;\n")
        grafo.write("bgcolor=\"#abb2b9\";\n")
        grafo.write("node[shape = \"ellipse\" style=filled fontname = \"Century Gothic\" color= \"#283747\"];\n")
        grafo.write("edge[arrowhead=vee color=\"#566573\" fontname=\"Sans-Serif\" fontsize=\"10\" penwidth=\"0.35\"];\n")
        for dato in z:
            grafo.write(dato)
        grafo.write('}')
        grafo.close()
        

    def mapa_sin_traza(self, lista_rutas, lista_estaciones, name):
        titulo = ''
        if name != '' and name != None:
            titulo = self.limpiar(name).capitalize()

        node = ''
        contenido = ''

        estacion = []
        d = 0
        for x in range(len(lista_estaciones)):
            a = self.get_estacion(lista_estaciones,d)
            b = self.get_estado(lista_estaciones,d)
            c = self.get_color(lista_estaciones,d)
            d += 3
            if a!=None and b!=None and c!=None:
                estacion.append([self.purificar(self.limpiar(a),"estacion"),self.purificar(self.limpiar(b),"estado"),self.purificar(self.limpiar(c),"color")])

        ruta = []
        e = 0
        for y in range(len(lista_rutas)):
            a = self.get_ruta(lista_rutas,e)
            b = self.get_peso(lista_rutas,e)
            c = self.get_inicio(lista_rutas,e)
            d = self.get_fin(lista_rutas,e)
            e += 4
            if a!=None and b!=None and c!=None and d!=None:
                ruta.append([self.purificar(self.limpiar(a),"ruta"),self.purificar(self.limpiar(b),"peso"),self.purificar(self.limpiar(c),"inicio"),self.purificar(self.limpiar(d),"fin")])


        directorio = str("Mapa")+'.dot'
        grafo = open(directorio,'w',encoding="utf8")
        grafo.write('digraph D {\n')
        grafo.write("rankdir=\"LR\";\n")
        grafo.write("splines=false;\n")
        grafo.write("bgcolor=\"#abb2b9\";\n")
        grafo.write("label=\"" + titulo + "\" fontname=\"Century Gothic\" labelloc=\"t\";\n")
        grafo.write("node[shape = \"ellipse\" style=filled fontname = \"Century Gothic\" color= \"#283747\"];\n")
        grafo.write("edge[arrowhead=vee color=\"#566573\" fontname=\"Sans-Serif\" fontsize=\"10\" penwidth=\"0.35\"];\n")
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if 'ESTACION' in estacion[i][j] and contenido == '':
                    node = estacion[i][j].replace('ESTACION','')
                    contenido = str(node) + '[label = \"'+estacion[i][j].replace('ESTACION','')
                elif 'ESTADO' in estacion[i][j] and contenido != '':
                    contenido = contenido + "\\n"+estacion[i][j].replace('ESTADO','')+"\""
                elif 'COLOR' in estacion[i][j] and contenido != '':
                    contenido = contenido + "  fillcolor=\""+ estacion[i][j].replace('COLOR','') +"\"];\n"
            grafo.write(contenido)
            
            contenido = ''
        
        recorrido = ''
        flecha = ''
        peso = ''
        for k in range(len(ruta)):
            for l in range(len(ruta[k])):
                if 'RUTA' in ruta[k][l]:
                    flecha = ruta[k][l].replace('RUTA','')
                if 'PESO' in ruta[k][l] or ruta[k][l].isdigit():
                    peso = ruta[k][l].replace('PESO','')
                if 'ESTACION' in ruta[k][l] and recorrido != '':
                    recorrido = recorrido + "->" + ruta[k][l].replace('ESTACION','')
                if 'ESTACION' in ruta[k][l] and recorrido=='':
                    recorrido = ruta[k][l].replace('ESTACION','')
            recorrido = recorrido + "[label = \""+ flecha + "\\n" + peso +"\"]\n"
            grafo.write(recorrido)
            recorrido = ''

        grafo.write('}')
        grafo.close()

        pre = directorio[:directorio.index('.dot')]
        os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
        os.startfile('\"'+pre+'.pdf\"')
        input("Mapa generado! Presione Enter para continuar...")

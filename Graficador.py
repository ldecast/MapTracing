import os

class Graficador:

    def get_nombre(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if 'nombre' in lista[indice].lower() and not 'estacion' in lista[indice].lower():
                    f = lista[indice].lower()
                    break
                else:
                    indice += 1
            return f
        except IndexError:
            return None

    def get_estacion(self, lista, indice):
        a = 0
        f = None
        try:
            while a < 4:
                a += 1
                if 'nombre' in lista[indice].lower() and not 'ruta' in lista[indice].lower():
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
        if tipo == "estacion" or tipo == "ruta" or tipo == "inicio" or tipo == "fin":
            f = lexema
            while(not f[0].isalpha()):
               f = f[1:]
            while(f[-1] != "_" and not f[-1].isalnum()):
               f = f[:-1]
            return f

        elif tipo == "estado":
            f = lexema
            while(f[0] != "d" and f[0] != "c"):
               f = f[1:]
            while(f[-1] != "e" and f[-1] != "a"):
               f = f[:-1]
            return f

        elif tipo == "color":
            f = lexema
            while(f[0] != "#"):
               f = f[1:]
            while(not f[-1].isalnum()):
               f = f[:-1]
            return f
        
        elif tipo == "peso":
            f = lexema
            while(not f[0].isnumeric()):
               f = f[1:]
            while(not f[-1].isnumeric()):
               f = f[:-1]
            return f
            
    
    def graficar_ruta(self, lista_rutas, lista_estaciones, eInicio, eFin):
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
                if eInicio == estacion[i][j]:
                    match1 = estacion[i][j]
        
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eFin == estacion[i][j]:
                    match2 = estacion[i][j]
        

        if match1 != "" and match2 != "":

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
                    if eInicio == estacion[i][j]:
                        match1 = estacion[i][j]
                    if eFin == estacion[i][j]:
                        match2 = estacion[i][j]
                    if 'estacion' in estacion[i][j] and contenido == '':
                        node = estacion[i][j]
                        contenido = str(node) + '[label = \"'+estacion[i][j]
                    elif 'disponible' in estacion[i][j] or 'cerrad' in estacion[i][j] and contenido != '':
                        contenido = contenido + "\\n"+estacion[i][j]+"\""
                    elif '#' in estacion[i][j] and contenido != '':
                        contenido = contenido + "  fillcolor=\""+ estacion[i][j] +"\"];\n"
                grafo.write(contenido)
                contenido = ''
            recorrido = ''
            flecha = ''
            peso = ''
            for k in range(len(ruta)):
                for l in range(len(ruta[k])):
                    if 'ruta' in ruta[k][l]:
                        flecha = ruta[k][l]
                    if '.' in ruta[k][l] or ruta[k][l].isdigit():
                        peso = ruta[k][l]
                    if 'estacion' in ruta[k][l] and recorrido != '':
                        recorrido = recorrido + "->" + ruta[k][l]
                    if 'estacion' in ruta[k][l] and recorrido=='':
                        recorrido = ruta[k][l]
                recorrido = recorrido + "[label = \""+ flecha + "\\n" + peso +"\"]\n"
                grafo.write(recorrido)
                recorrido = ''

            grafo.write('}')
            grafo.close()

            self.ruta_rapida(match1,match2,directorio)
            
            self.revisar(directorio)
            
            pre = directorio[:directorio.index('.dot')]
            os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
            os.startfile('\"'+pre+'.pdf\"')
            input("Ruta generada! Presione Enter para continuar...")

        else:
            print("No se ha podido reconocer una estación válida. Por favor intente de nuevo.")
            input("Presione Enter para continuar...")

    def graficar_mapa(self, lista_rutas, lista_estaciones, eInicio, eFin, name):
        
        if name != '' and name != None:
            titulo = self.limpiar(name)

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
                if eInicio == estacion[i][j]:
                    match1 = estacion[i][j]
        
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                if eFin == estacion[i][j]:
                    match2 = estacion[i][j]
        

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
                    if eInicio == estacion[i][j]:
                        match1 = estacion[i][j]
                    if eFin == estacion[i][j]:
                        match2 = estacion[i][j]
                    if 'estacion' in estacion[i][j] and contenido == '':
                        node = estacion[i][j]
                        contenido = str(node) + '[label = \"'+estacion[i][j]
                    elif 'disponible' in estacion[i][j] or 'cerrad' in estacion[i][j] and contenido != '':
                        contenido = contenido + "\\n"+estacion[i][j]+"\""
                    elif '#' in estacion[i][j] and contenido != '':
                        contenido = contenido + "  fillcolor=\""+ estacion[i][j] +"\"];\n"
                grafo.write(contenido)
                
                contenido = ''
            
            recorrido = ''
            flecha = ''
            peso = ''
            for k in range(len(ruta)):
                for l in range(len(ruta[k])):
                    if 'ruta' in ruta[k][l]:
                        flecha = ruta[k][l]
                    if '.' in ruta[k][l] or ruta[k][l].isdigit():
                        peso = ruta[k][l]
                    if 'estacion' in ruta[k][l] and recorrido != '':
                        recorrido = recorrido + "->" + ruta[k][l]
                    if 'estacion' in ruta[k][l] and recorrido=='':
                        recorrido = ruta[k][l]
                recorrido = recorrido + "[label = \""+ flecha + "\\n" + peso +"\"]\n"
                grafo.write(recorrido)
                recorrido = ''

            grafo.write('}')
            grafo.close()

            self.ruta_rapida(match1,match2,directorio)
                    
            pre = directorio[:directorio.index('.dot')]
            os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
            os.startfile('\"'+pre+'.pdf\"')
            input("Mapa generado! Presione Enter para continuar...")
        
        else:
            print("No se ha podido reconocer una estación válida. Por favor intente de nuevo.")
            input("Presione Enter para continuar...")
    
    def ruta_rapida(self, inicio, fin, dot):
        reader = open(dot,'r')
        rutas_posibles = []
        cerradas = []
        done = False
        for linea in reader.readlines():
            if 'cerrad' in linea:
                cerradas.append(linea[:linea.index('[')])
            if inicio == fin:
                done = True
                break
            elif str(inicio+'->') in linea:
                rutas_posibles.append(linea)
            elif str('->'+fin) in linea:
                rutas_posibles.append(linea)

        for cerrado in cerradas:
            for posible in rutas_posibles:
                if cerrado in posible:
                    rutas_posibles.remove(posible)

        reader.close()
        if done == False:
            self.evaluar(rutas_posibles,inicio,fin,dot)
            
        
    def evaluar(self,linea, inicio, fin,dot):
        nuevo_inicio = ''
        peso = []
        ruta_vieja = ''
        ruta_pintar = ''
        fast = ''
        for dato in linea:
            if str(inicio+'->') in dato:
                peso.append(dato[dato.rfind('\\n')+2:dato.rfind('"')])
        if peso!= []:
            fast = min(peso)
            for dato in linea:
                if str(fast) == dato[dato.rfind('\\n')+2:dato.rfind('"')]:
                    nuevo_inicio = dato[dato.index('>')+1:dato.index('[')]
                    ruta_vieja = dato
                    ruta_pintar = dato.replace(']',' penwidth=\"2\" color=\"#196f3d\"]')
            # print(nuevo_inicio)
            self.ruta_rapida(nuevo_inicio,fin,dot)
            self.sobre_escribir(dot,ruta_vieja,ruta_pintar)
        else:
            return False


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
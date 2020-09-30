import csv
import os

class Graficador:

    def reportar(self, datos):
        errores = ["No.","Fila","Columna","Caracter","Descripcion"]
        datos.insert(0,errores)
        csv_file = open('Lista de errores.csv', 'w', newline='', encoding="utf-8")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)
        print("Reporte de errores generado!")
    
    def tokens(self, datos):
        encabezado = ["No.","Lexema","Fila","Columna","Token"]
        datos.insert(0,encabezado)
        csv_file = open('Lista de tokens.csv', 'w', newline='', encoding="utf-8")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)    
        print("Reporte de tokens generado!")

    # def get_estacion(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 4:
    #             a += 1
    #             if 'estacion' in lista[indice].lower():
    #                 f = lista[indice].lower()
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None
    # def get_estado(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 4:
    #             a += 1
    #             if 'disponible' in lista[indice].lower() or 'cerrad' in lista[indice].lower():
    #                 f = lista[indice].lower()
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None
    # def get_color(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 4:
    #             a += 1
    #             if '#' in lista[indice]:
    #                 f = lista[indice]
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None
    
    # def get_ruta(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 5:
    #             a += 1
    #             if 'ruta' in lista[indice].lower():
    #                 f = lista[indice].lower()
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None
    
    # def get_peso(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 5:
    #             a += 1
    #             if str(lista[indice]).isdigit() or '.' in lista[indice]:
    #                 f = lista[indice]
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None

    # def get_inicio(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 5:
    #             a += 1
    #             if 'estacion' in lista[indice].lower():
    #                 f = lista[indice].lower()
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None

    # def get_fin(self, lista, indice):
    #     a = 0
    #     f = None
    #     try:
    #         while a < 5:
    #             a += 1
    #             if 'estacion' in lista[indice].lower():
    #                 f = lista[indice].lower()
    #                 break
    #             else:
    #                 indice += 1
    #         return f
    #     except IndexError:
    #         return None

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
    
    def limpiar(self, lexema):
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
    
    def graficar_ruta(self, lista_rutas, lista_estaciones, eInicio, eFin):
        pass
        # print(lista_rutas)

    def graficar_mapa(self, lista_rutas, lista_estaciones, eInicio, eFin):
        # print(lista_estaciones)
        # print(lista_rutas)
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
                estacion.append([self.limpiar(a),self.limpiar(b),self.limpiar(c)])
        # print(estacion)

        ruta = []
        
        e = 0
        for y in range(len(lista_rutas)):
            a = self.get_ruta(lista_rutas,e)
            b = self.get_peso(lista_rutas,e)
            c = self.get_inicio(lista_rutas,e)
            d = self.get_fin(lista_rutas,e)
            e += 4
            if a!=None and b!=None and c!=None and d!=None:
                ruta.append([self.limpiar(a),self.limpiar(b),self.limpiar(c),self.limpiar(d)])
        # print(ruta)

        match1 = ''
        match2 = ''

        # for i in range(len(estacion)):
        #     for j in range(len(estacion[i])):
        #         # print(estacion[i][j])
        #         if eInicio == estacion[i][j]:
        #             match1 = estacion[i][j]
        
        # for i in range(len(estacion)):
        #     for j in range(len(estacion[i])):
        #         # print(estacion[i][j])
        #         if eFin == estacion[i][j]:
        #             match2 = estacion[i][j]
        

        

        # if match1 != '' and match2 != '':
        #     self.ruta_rapida(match1,match2,directorio)
        directorio = str(match1 + "-" + match2)+'.dot'
        grafo = open(directorio,'w',encoding="utf-8")
        grafo.write('digraph D {\n')
        grafo.write("rankdir=\"LR\";\n")
        grafo.write("node[shape = \"ellipse\" style=filled fontname = \"Century Gothic\" color= \"#283747\"];\n")
        grafo.write("edge[arrowhead=vee color=\"#a6acaf \" fontname=\"Sans-Serif\" fontsize=\"10\"];\n")
        for i in range(len(estacion)):
            for j in range(len(estacion[i])):
                # print(estacion[i][j])
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
            # print(contenido)
            contenido = ''
        rutas_posibles = []
        posible = False
        recorrido = ''
        flecha = ''
        peso = ''
        hola = []
        for k in range(len(ruta)):
            for l in range(len(ruta[k])):
                # print(ruta[k][l])
                if eInicio == ruta[k][l]:
                    posible = True
                    rutas_posibles.append(k)
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
            # hola.append(recorrido)
            recorrido = ''
        # print(hola)
        
        # if posible != False:
        #     # rutas_posibles.append(posible)
        #     print(rutas_posibles)
        #     for k in rutas_posibles:
        #         for l in range(len(ruta[k])):
        #             print(ruta[k][l])



                
        grafo.write('}')

        grafo.close()
        pre = directorio[:directorio.index('.dot')]
        os.system('dot -Tpdf \"'+directorio+'\" -o \"Mapa ['+pre+'].pdf\"')
        os.startfile('\"Mapa ['+pre+'].pdf\"')
    
    def ruta_rapida(self, inicio, fin, dot):
        reader = open(dot,'r')
        rutas_posibles = []
        aux_posibles = []
        for linea in reader.readlines():
            print(linea)
            if str('->'+fin) in linea:
                rutas_posibles.append(linea[:'['])
        
        for linea in reader.readlines():
            if str(inicio+'->') in linea:
                aux_posibles.append(linea[inicio:'['])

        print(rutas_posibles)
        print(aux_posibles)
        # if rutas_posibles!=None:
        #     for dato in rutas_posibles:
        #         if inicio in 

        reader.close()
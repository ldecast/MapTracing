# # frase = "<ruta><nombre>"
# # a = [idx for idx, x in enumerate(frase) if x=='<']
# # b = [idx for idx, x in enumerate(frase) if x=='>']
# # print(frase[a.pop()+1:b.pop()])

# # a = ["H", "O", "L", "A"]
# # b = []
# # for i in range(len(a)):
# #     b.append(a[i].lower())
# # print(b)

# def get_estacion(lista, indice):
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

# def get_estado(lista, indice):
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
#                 print(lista[indice])
#         return f
#     except IndexError:
#         return None
# def get_color(lista, indice):
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
# lista = ['EstacionZona6', 'disponible', '#1A5AAF', '#AF5B1A', 'EstacionZona2', 'disponible', 'EstacionZona1', '#E52E22', 'disponible','estacion5','#32323S']
# estacion = []
# d=0
# for j in range(9):
#     a = get_estacion(lista,d)
#     b = get_estado(lista,d)
#     c = get_color(lista,d)
#     d += 3
#     if a!=None and b!=None and c!=None:
#         estacion.append([a,b,c])
#     # elif a == None:
#     #     print(lista[j])
#     elif b == None:
#         print(lista[j])
#     # elif c == None:
#     #     print(lista[j])
# print(estacion)


# lista = [['estacionzona6', 'disponible', '#1A5AAF'], ['estacionzona2', 'disponible', '#AF5B1A'], ['estacionzona1', 'disponible', '#E52E22']]
# node = -1
# contenido = ''
# for i in range(len(lista)):
#     for j in range(len(lista[i])):
#         print(lista[i][j])
#     print("stop")

# lista = 5
# # print(str(lista).isdigit())
# for z in range(5):
#     print(lista)










# caracter = "”"
# lexema = "<inicio>”estacionzona2</inicio>"
# lexema = lexema.replace(caracter,'')
# print(lexema)







import time



def sobre_escribir(dot,ruta_vieja,ruta_nueva):
    reader = open(dot,'r')
    lineas = []
    # new = []
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





def evaluar(linea, inicio, fin,dot):
    # print(inicio)
    nuevo_inicio = ''
    peso = []
    ruta_pintar = ''
    ruta_vieja = ''
    fast = ''
    intento2 = []
    for dato in linea:
        # if str(inicio+'->') in dato:
            # peso.append(dato[dato.rfind('\\n')+2:dato.rfind('"')])
        nuevo_inicio = dato[dato.index('>')+1:dato.index('[')]
        intento2.append(nuevo_inicio)

        # elif str(inicio+'->'+fin) in dato:

            # print(peso)
    # fast = min(peso)
    # print(fast)

 #   # for dato in linea:
    #     # print(dato,'dato')
    #     if str(fast) == dato[dato.rfind('\\n')+2:dato.rfind('"')]:
    #         nuevo_inicio = dato[dato.index('>')+1:dato.index('[')]
    #         ruta_vieja = dato
 #   #         ruta_pintar = dato.replace(']',' penwidth="2" color=\"green\"]')
    print(intento2,"jeje")
    # if nuevo_inicio != fin:
    ruta_rapida(intento2,fin,dot)
    # sobre_escribir(dot,ruta_vieja,ruta_pintar)

    

def ruta_rapida(inicio, fin, dot):
    reader = open(dot,'r')
    rutas_posibles = []
    aux_posibles = []
    # for linea in reader.readlines():
    #     # print(linea)
    #     if str('->'+fin) in linea:
    #         rutas_posibles.append(linea[:linea.index('[')])
    #     elif str(inicio+'->') in linea:
    #         aux_posibles.append(linea[:linea.index('[')])
    cerradas = []
    done = False
    for a in inicio:
        for linea in reader.readlines():
            if 'cerrad' in linea:
                cerradas.append(linea[:linea.index('[')])
            if a == fin:
                done = True
                print("llego a su destino",a)
                break
            if str(a+'->'+fin) in linea:
                aux_posibles.append(linea)
                
            elif str(a+'->') in linea:
                rutas_posibles.append(linea)
        
            
        # elif str('->'+fin) in linea:
        #     rutas_posibles.append(linea)
        

    for cerrado in cerradas:
        for posible in rutas_posibles:
            if cerrado in posible:
                # print(cerrado)
                # print(posible)
                rutas_posibles.remove(posible)
    # print(rutas_posibles)


    # print(rutas_posibles)
        # print(aux_posibles)
        # if rutas_posibles!=None:
        #     for dato in rutas_posibles:
        #         if inicio in 

    reader.close()
    print(rutas_posibles)
    # print(aux_posibles)
    # for posible in rutas_posibles:
    if done == False:
        evaluar(rutas_posibles,inicio,fin,dot)

ruta_rapida(['estacionzona6'],'estacionzona5','ok-ok.dot')
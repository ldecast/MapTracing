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










caracter = "”"
lexema = "<inicio>”estacionzona2</inicio>"
lexema = lexema.replace(caracter,'')
print(lexema)
















# def evaluar()




# def ruta_rapida(inicio, fin, dot):
#         reader = open(dot,'r')
#         rutas_posibles = []
#         aux_posibles = []
#         # for linea in reader.readlines():
#         #     # print(linea)
#         #     if str('->'+fin) in linea:
#         #         rutas_posibles.append(linea[:linea.index('[')])
#         #     elif str(inicio+'->') in linea:
#         #         aux_posibles.append(linea[:linea.index('[')])
        
#         for linea in reader.readlines():
#             if str(inicio+'->') in linea:
#                 rutas_posibles.append(linea)
#             elif str('->'+fin) in linea:
#                 rutas_posibles.append(linea)

#         # for posible in rutas_posibles:
#         #     for aux in aux_posibles:
#         #         if 

#         print(rutas_posibles)
#         print(aux_posibles)
#         # if rutas_posibles!=None:
#         #     for dato in rutas_posibles:
#         #         if inicio in 

#         reader.close()

# ruta_rapida('estacionzona6','estacionzona1','hola-adios.dot')
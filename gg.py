frase = "<ruta><nombre>"
a = [idx for idx, x in enumerate(frase) if x=='<']
b = [idx for idx, x in enumerate(frase) if x=='>']
print(frase[a.pop()+1:b.pop()])
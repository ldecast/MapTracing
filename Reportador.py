import csv

class Reportador:

    def error(self, datos):
        errores = ["No.","Fila","Columna","Caracter","Descripcion"]
        datos.insert(0,errores)
        csv_file = open('Lista de errores.csv', 'w', newline='', encoding="utf-8-sig")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)
        print("Reporte de errores generado!")


    def tokens(self, datos):
        encabezado = ["No.","Lexema","Fila","Columna","Token"]
        datos.insert(0,encabezado)
        csv_file = open('Lista de tokens.csv', 'w', newline='', encoding="utf-8-sig")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)    
        print("Reporte de tokens generado!")

import csv

class Graficador:

    def reportar(self, datos):
        errores = ["No.","Fila","Columna","Caracter","Descripción"]
        datos.insert(0,errores)
        csv_file = open('Lista de errores.csv', 'w')
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)
        print("Reporte de errores generado!")
    



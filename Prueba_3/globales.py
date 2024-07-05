import json
import csv

def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

# leer archivo json
def leer_archivo_json(productos):
    try:
        with open(productos, 'r', "productos.json") as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que quenga el archivo
    except:
        return []

def guardar_archivo_json(productos, data):
    try:
        with open(productos, 'w', ) as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return []

def ver_estadisticas(productos, data):
    try:
        with open(productos, 'r', "productos.json" ) as archivo: # Ver las estadisticas 
            json.dump(data, archivo, indent=4)
    except:
        return []

for i in productos(15):
    return

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []


def listado_tabla(array, headers):
    col_widths = [max(len(header), 15) + 2 for header in headers]
    
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for data in array:
        row = ' | '.join(f"{str(data.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)

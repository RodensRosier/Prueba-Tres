import os
import globales

os.system("cls")

def menu_principal():
    print("=============== Menu Prinpcipal ===============")
    print("1. Asignar Montos Aleatrorios")
    print("2. Ver Estadisticas")
    print("3. Salir del programa")

    def seleccionar_opcion(max_value):
         opcion == 0
    while True:
        try:
            opcion = int(input("Por favor ingrese una opción: "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, por favor intente nuevamente: ")
        else:
            return opcion

        if menu_principal == 1:
            open.globales.leer_archivo_json(dir, 'w', "productos.json") 
        if menu_principal == 2:
            open.globales.ver_estadisticas(dir, 'r', "productos.json")
        else:
             return

    menu_principal()
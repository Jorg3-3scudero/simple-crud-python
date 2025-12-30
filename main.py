#imports
import json
from functions import consultar_precio, agg_producto, actualizar_producto, eliminar_producto, catalogo #importamos las funciones desde el modulo funciones

def main():
    with open("data.json", "r") as data: #abrimos el archivo json y lo leemos con "r", y ponemos esta informacion en el dict precios
        precios = json.load(data)


    while True:
        print("\n----------MENU----------")#opciones para usuario
        print("1. Consultar precios")
        print("2. Agregar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Ver catálogo completo")
        print("6. Salir")

        opcion = input("Ingrese una opcion: ")#input usuario para opciones

        if opcion == "1": #consultar precio
            consultar_precio(precios)
        elif opcion == "2": #agregar producto
            agg_producto(precios)
            with open("data.json", "w") as data:
                json.dump(precios, data, indent=4)
        elif opcion == "3": #actualizar producto
            actualizar_producto(precios)
            with open("data.json", "w") as data:
                json.dump(precios, data, indent=4)
        elif opcion == "4":
            eliminar_producto(precios)
            with open("data.json", "w") as data:
                json.dump(precios, data, indent=4)
        elif opcion == "5":
            catalogo(precios)
        elif opcion == "6":
            print("Gracias por usar el sistema CRUD!")
            break
        else:
            print("opcion no valida, ingresela nuevamente")    

if __name__=='__main__':
    main()

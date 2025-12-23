#CRUD SIMPLE SIN BASE DE DATOS NI STOCK DE ITEMS
#diccionario precios

from functions import consultar_precio, agg_producto, actualizar_producto, eliminar_producto, catalogo

precios = {"leche": 5000,
           "queso": 4500,
           "salchicha": 6200,
           "huevos x 12": 10000,
           "dulce": 500}

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
    elif opcion == "3": #actualizar producto
        actualizar_producto(precios)
    elif opcion == "4":
        eliminar_producto(precios)
    elif opcion == "5":
        catalogo(precios)
    elif opcion == "6":
        print("Gracias por usar el sistema CRUD!")
        break
    else:
        print("opcion no valida, ingresela nuevamente")    

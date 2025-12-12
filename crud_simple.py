#CRUD SIMPLE SIN BASE DE DATOS NI STOCK DE ITEMS
#diccionario precios
precios = {"leche": 5000,
           "queso": 4500,
           "salchicha": 6200,
           "huevos x 12": 10000,
           "dulce": 500}

#inicializacion variable menu para el lopp
menu = True


while menu:
    print("\n----------MENU----------")#opciones para usuario
    print("1. Consultar precios")
    print("2. Agregar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Ver catálogo completo")
    print("6. Salir")

    opcion = input("Ingrese una opcion: ")#input usuario para opciones

    if opcion == "1": #consultar precio
        while True:
            user = input("Ingrese el producto el cual quiera saber el precio(presione 'q' para salir): ").lower()
            if user == "q":
                break
            elif precios.get(user) is not None: #si el get no arroja none, mostrar el valor segun la clave dada de el usuario
                print(f"vale: {precios[user]:,}")
            else:
                print("Dato ingresado no valido, ingreselo nuevamente")
    elif opcion == "2": #agregar producto
            while True:#loop para que el usuario siga agrando items a gusto hasta dada la condicion "q"
                clave = input("Ingrese el item a agregar ('q' para salir): ").lower()
                if clave == "q":
                    break
                valor = input("Ingrese el precio del item: ")
                while not valor.isdigit(): #verificacion precio es digito
                    print("Por favor ingrese un precio válido")
                    valor = input("Ingrese el precio del item: ")
                valor = int(valor)
        
                precios[clave] = valor
                print(f"✓ {clave} agregado con precio ${valor}")
                # El bucle continúa, preguntará de nuevo si el usuarioquiere agregar otro
    elif opcion == "3":
           while True:#loop para que el usuario siga agrando items a gusto hasta dada la condicion "q"
            key_update = input("Ingrese el item a actualizar ('q' para salir): ").lower()
            if key_update == "q":
                break
        
            if key_update in precios: #loop para checkear que el producto exista o no en el sistema 
                print(f"Precio actual: ${precios[key_update]:,}")
                value_update = input("Ingrese el precio nuevo: ")
                while not value_update.isdigit():
                    print("Precio no válido, inténtelo de nuevo")
                    value_update = input("Ingrese el precio nuevo: ")
                value_update = int(value_update)
                precios[key_update] = value_update
                print(f"✓ {key_update} actualizado a ${value_update:,}")
            else:
                print(f"'{key_update}' no existe en la tienda.")
    elif opcion == "4":
        while True:#loop para que el usuario siga agrando items a gusto hasta dada la condicion "q"
            key_delete = input("Ingrese el item a eliminar ('q' para salir): ").lower()
            if key_delete == "q":
                break
        
            if key_delete in precios: #loop para eliminar objeto de la tienda, pide confirmacion de usuario
                confirmar = input(f"¿Seguro que desea eliminar '{key_delete}' (${precios[key_delete]:,})? (si/no): ").lower()
                if confirmar == "si":
                    precios.pop(key_delete)
                    print(f"✓ {key_delete} eliminado correctamente")
                else:
                    print("Eliminación cancelada")
            else:
                print(f"'{key_delete}' no existe en la tienda.")
    elif opcion == "5":
        if not precios:
            print(" El catálogo está vacío")
        else:
            print("\n===== CATÁLOGO COMPLETO =====")
        for item, precio in precios.items(): #for loop con precios.items() para mostrar todo el catalogo de la tienda
            print(f"{item.capitalize()}: ${precio:,}")
        print(f"\nTotal de productos: {len(precios)}") #mostrar la cantidad de productos en el catalogo
        print("=============================")
    elif opcion == "6":
        print("Gracias por usar el sistema CRUD!")
        break
    else:
        print("opcion no valida, ingresela nuevamente")    

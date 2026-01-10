#imports
from functions import Tienda
from utils import verification, empty_validation, confirm_action

def main():
    tienda = Tienda("data.json")

    while True:
        print("\n----------MENU----------")#opciones para usuario
        print("1. Consultar precios")
        print("2. Agregar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Ver catálogo completo")
        print("6. Salir")

        opcion = input("Ingrese una opcion: ").strip()#input usuario para opciones

        if opcion == "1": #consultar precio
            while True:
                user = input("Ingrese el producto (q para salir): ").lower()
                if user == "q":
                    break
                precio = tienda.consultar_precios(user)
                if precio is not None:
                    print(f"{user.capitalize()}: ${precio:,}")
                else:
                    print("Dato ingresado no válido")
        elif opcion == "2": #agregar producto
            while True:
                clave = empty_validation("Ingrese el item a agregar")
                if clave is None:
                    break
                
                # Verificar si ya existe
                if tienda.producto_existe(clave):
                    precio_actual = tienda.consultar_precios(clave)
                    print(f" {clave.capitalize()} ya existe con precio ${precio_actual:,}")
                    
                    
                    if not confirm_action("¿Desea sobrescribirlo?"):
                        print("Operación cancelada")
                        continue  # Vuelve a pedir otro producto
                
                # Si llegaste aquí, o no existía o el usuario confirmó sobrescribir
                valor = verification()
                tienda.agregar_producto(clave, valor)
                print(f"{clave.capitalize()} agregado con precio ${valor:,}")
        elif opcion == "3": #actualizar producto
            while True:
                keyupdate = input("Ingrese el item a actualizar (q para salir): ").lower()
                if keyupdate == "q":
                    break
                if keyupdate in tienda.precios:
                    print(f"Precio actual: ${tienda.precios[keyupdate]:,}")
                    valueupdate = verification()
                    tienda.actualizar_producto(keyupdate, valueupdate)
                    print(f"{keyupdate.capitalize()} actualizado a ${valueupdate:,}")
                else:
                    print(f"{keyupdate.capitalize()} no existe")
        elif opcion == "4":
            while True:
                keydelete = input("Ingrese el item a eliminar (q para salir): ").lower()
                if keydelete == "q":
                    break
                if keydelete in tienda.precios:
                    confirmar = input(f"¿Seguro que desea eliminar {keydelete.capitalize()}? (si/no): ").lower()
                    if confirmar == "si":
                        tienda.eliminar_producto(keydelete)
                        print(f"{keydelete.capitalize()} eliminado correctamente")
                    else:
                        print("Eliminación cancelada")
                else:
                    print(f"{keydelete.capitalize()} no existe")
        elif opcion == "5":
            precios = tienda.catalogo_completo()
            if not precios:
                print("El catálogo está vacío")
            else:
                print()
                print("CATÁLOGO COMPLETO")
                for item, precio in precios.items():
                    print(f"{item.capitalize()}: ${precio:,}")
                print(f"\nTotal de productos: {len(precios)}")
        elif opcion == "6":
            print("Gracias por usar el sistema CRUD!")
            break
        else:
            print("opcion no valida, ingresela nuevamente")    

if __name__=='__main__':
    main()


#TODO ADD VALIDATION OF INPUT ON ALL THE OPTIONS


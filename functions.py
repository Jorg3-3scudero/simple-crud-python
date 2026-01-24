#funciones
import json
import os

class Tienda: #made all class related methods for scalability
    def __init__(self, archivo_datos="data.json"):
        self.archivo_datos = archivo_datos

        if not os.path.exists(self.archivo_datos):
            self.precios = {}
            self.guardar_datos()
        else:
            try:
                with open(self.archivo_datos, "r") as data:
                    self.precios = json.load(data)
            except json.JSONDecodeError:
                print(f"⚠️  {self.archivo_datos} está corrupto. Creando uno nuevo.")
                self.precios = {}
                self.guardar_datos()

    def guardar_datos(self): #upgraded to have a method for saving data on the functions module, for cleaner readbility
        try:
            with open(self.archivo_datos, "w") as data:
                json.dump(self.precios, data, indent=4)
            return True
        except PermissionError:
            print(f"Error: no tienes permisos para escribir en el archivo {self.archivo_datos}")
        except OSError as e:
            #captura otros erroes de el sistema operativo
            print(f"Error inesperado al guardar el archivo: {e}")
            return False


    def consultar_precios(self, producto: str) -> int | None: #if the product is in the dict of precios, then return the desired producto, if not, return none
        try:
            return self.precios[producto]
        except KeyError:
            print(f'Error: el producto: {producto} no existe')
        return None #retorna none como una forma de señalizacion entre functions.py y main.py

    def agregar_producto(self, producto: str, precio: int): #from user input, 
            self.precios[producto] = precio

            return self.guardar_datos()

    def actualizar_producto(self, producto: str, nuevo_precio: int):
        if producto in self.precios:
            self.precios[producto] = nuevo_precio
            return self.guardar_datos()
        return False

    def eliminar_producto(self, producto: str):
        try:
            del self.precios[producto]
            return self.guardar_datos()
        except KeyError:
            print(f'Error: el producto {producto} no existe')
            return False

    def catalogo_completo(self):
        return self.precios
    
    def producto_existe(self, producto):
        return producto in self.precios
    
    def __contains__(self, key):
        return key in self.precios
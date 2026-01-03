#funciones
import json

class Tienda: #made all class related methods for scalability
    def __init__(self, archivo_datos="data.json"):
        self.archivo_datos = archivo_datos
        with open(self.archivo_datos, "r") as data:
            self.precios = json.load(data)

    def guardar_datos(self): #upgraded to have a method for saving data on the functions module, for cleaner readbility
        with open(self.archivo_datos, "w") as data:
            json.dump(self.precios, data, indent=4)

    def consultar_precios(self, producto): #if the product is in the dict of precios, then return the desired producto, if not, return none
        if producto in self.precios:
            return self.precios[producto]
        return None

    def agregar_producto(self, producto, precio): #from user input, 
        self.precios[producto] = precio
        self.guardar_datos()

    def actualizar_producto(self, producto, nuevo_precio):
        if producto in self.precios:
            self.precios[producto] = nuevo_precio
            self.guardar_datos()

    def eliminar_producto(self, producto):
        if producto in self.precios:
            self.precios.pop(producto)
            self.guardar_datos()

    def catalogo_completo(self):
        return self.precios
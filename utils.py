def verification():
    while True:
        valor = input("Ingrese el precio del item: ").strip()
    
        try:
            precio = int(valor)
            if precio > 0:
                return precio
            print('El valor debe ser mayor a 0')
        except ValueError:
            print('Error: porfavor ingrese solo numeros')

def empty_validation(mensaje):
    while True:
        valor = input(f"{mensaje} (q para salir): ").lower().strip()
        if valor == "q":
            return None
        if not valor:
            print("El valor no puede estar vacío")
            continue
        return valor
    
def confirm_action(mensaje):
    respuesta = input(f"{mensaje} (si/no): ").lower().strip()
    return respuesta in ["si", "sí", "s", "yes"]
def verification():
    while True:
        valor = input("Ingrese el precio del item: ").strip()
        
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        
        print("Ingrese un precio válido (número mayor a 0)")

def empty_validation(mensaje):
    while True:
        valor = input(f"{mensaje} (q, para salir): ").lower().strip()
        if valor == "q":
            return None
        if not valor:
            print("El valor no puede estar vacío")
            continue
        return valor
    
def confirm_action(mensaje):
    respuesta = input(f"{mensaje} (si/no): ").lower().strip()
    return respuesta in ["si", "sí", "s", "yes"]
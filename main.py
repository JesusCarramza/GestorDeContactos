import os
import time

def agregar_contacto():
    print("Agregar contacto")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    email = input("Email: ")

    contacto = {
        "id": len(agenda) + 1,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

def ver_contactos():
    print("\nLista de contactos:")
    if not agenda:
        print("No hay contactos guardados.")
    else:
        for contacto in agenda:
            print(f"ID: {contacto['id']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            print("-" * 20)


    agenda.append(contacto)

    print("Contacto agregado")

def menu():
    print("Bienvenido a la agenda de contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Cargar contactos desde archivo")
    print("7. Guardar contactos en archivo")
    print("8. Salir")

def limpiar_pantalla():
    time.sleep(2)
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    global agenda
    agenda = []
    global system
    if os.name == "nt":
        system = "Windows"
    else:
        system = "Linux"
    menu()
    while True:
        opcion = input("Opcion: ")
        if opcion == "1":
            agregar_contacto()
            limpiar_pantalla()
        elif opcion == "2":
            ver_contactos()


if __name__ == "__main__":
    main()
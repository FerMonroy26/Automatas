def registrar_usuario():
    print("Bienvenido al sistema de registro de usuarios.")
    nombres = input("Ingrese su(s) nombre(s): ")
    apellidos = input("Ingrese su(s) apellido(s): ")
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")

    print("\nRegistrando usuario...\n")
    # Aquí podrías agregar código para guardar los datos en una base de datos o en algún otro lugar, pero por ahora solo los imprimiremos
    print("Usuario registrado con éxito.")

    # Dar la bienvenida al usuario
    print("\n¡Hola {}, en breve recibirás un correo a {}!".format(nombres + " " + apellidos, correo))

def main():
    registrar_usuario()

if __name__ == "__main__":
    main()

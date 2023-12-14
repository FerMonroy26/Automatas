import unidecode;
from unidecode import unidecode

def analizar_palabra(palabra):
    # Quitar acentos usando unidecode
    palabra_sin_acentos = unidecode(palabra)

    # Determinar si la palabra original es igual a la palabra sin acentos
    tiene_acentos = palabra != palabra_sin_acentos

    # Determinar el tipo de palabra
    tipo_palabra = "con acentos" if tiene_acentos else "sin acentos"

    return tipo_palabra

# Programa principal
while True:
    palabra = input("Ingrese una palabra (o escriba EXIT para salir): ").strip().upper()

    if palabra == "EXIT":
        print("Programa finalizado.")
        break

    tipo_palabra = analizar_palabra(palabra)
    print(f"La palabra '{palabra}' es {tipo_palabra}.\n")


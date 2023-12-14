def tipo_palabra(palabra):
    vocales_acentuadas = "áéíóú"
    palabra = palabra.lower()
    
    # Buscar la posición de la sílaba tónica
    silaba_tonica = 0
    for i, letra in enumerate(palabra):
        if letra in vocales_acentuadas:
            silaba_tonica = i
    
    # Determinar el tipo de palabra
    if silaba_tonica == len(palabra) - 1:
        return "aguda"
    elif silaba_tonica == len(palabra) - 2:
        return "grave"
    elif silaba_tonica == len(palabra) - 3:
        return "esdrújula"
    elif silaba_tonica == len(palabra) - 4:
        return "sobresdrújula"
    else:
        return "otro tipo"

# Programa principal
while True:
    palabra = input("Ingrese una palabra (o escriba EXIT para salir): ").strip().upper()

    if palabra == "EXIT":
        print("Programa finalizado.")
        break

    tipo = tipo_palabra(palabra)
    print(f"La palabra '{palabra}' es {tipo}.\n")

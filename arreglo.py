def buscar_en_arreglo(arreglo, arreglo_busca):
    encontrados = []
    for indice, numero in enumerate(arreglo):
        if numero in arreglo_busca:
            encontrados.append((numero, indice))
    
    if len(encontrados) > 0:
        return encontrados
    else:
        return "No se encontraron coincidencias."

# Ejemplo de uso:
arreglo1 = [1, 2, 3, 4, 5]
arreglo2 = [2, 5, 6, 7, 1]

fuente_datos = input("Escoja la fuente de datos (escriba 1 para arreglo1 y 2 para arreglo2): ")

if fuente_datos == '1':
    resultado = buscar_en_arreglo(arreglo1, arreglo2)
elif fuente_datos == '2':
    resultado = buscar_en_arreglo(arreglo2, arreglo1)
else:
    resultado = "Selección no encontrada."

print(resultado)

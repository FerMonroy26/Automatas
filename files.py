import csv
import re

def validar_tipo_dato(dato, tipo):
    if tipo == "numerico":
        return dato.isdigit()
    elif tipo == "alfa":
        return dato.isalpha()
    elif tipo == "correo":
        # Validar dirección de correo electrónico usando una expresión regular
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, dato) is not None
    elif tipo == "curp":
        # Validar CURP (Clave Única de Registro de Población) usando una expresión regular
        curp_regex = r'^[A-Z]{4}[0-9]{6}[HM][A-Z]{5}[A-Z0-9]{2}$'
        return re.match(curp_regex, dato) is not None
    else:
        return False

def validar_csv(archivo):
    with open(archivo, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        cabecera = next(csvreader)  # Obtener la primera fila como cabecera
        num_columnas = len(cabecera)
        errores = []
        
        for fila_num, fila in enumerate(csvreader, start=2):
            # Verificar cantidad de columnas
            if len(fila) != num_columnas:
                errores.append(f"Fila {fila_num}: Cantidad incorrecta de columnas.")
            else:
                # Verificar si las columnas tienen datos y el tipo de datos es correcto
                for col_num, (dato, tipo) in enumerate(zip(fila, cabecera), start=1):
                    if not dato:
                        errores.append(f"Fila {fila_num}, Columna {col_num}: Dato faltante.")
                    elif not validar_tipo_dato(dato, tipo):
                        errores.append(f"Fila {fila_num}, Columna {col_num}: Tipo de dato incorrecto.")
                        
        if errores:
            print("Errores encontrados:")
            for error in errores:
                print(error)
        else:
            print("El archivo CSV cumple con las especificaciones.")

# Llamar a la función y pasar el nombre del archivo CSV que quieres validar
archivo_csv = 'tu_archivo.csv'
validar_csv(archivo_csv)

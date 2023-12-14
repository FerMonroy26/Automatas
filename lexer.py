import re

# Definir las expresiones regulares para los tokens
tokens = [
    r'SELECT',
    r'INSERT',
    r'UPDATE',
    r'DELETE',
    r'FROM',
    r'WHERE',
    r'JOIN',
    r'ON',
    r'AND',
    r'OR',
    r'NOT',
    r'[0-9]+',        # Números
    r'[a-zA-Z_]\w*',  # Identificadores
    r'=',             # Operador de comparación
    r'<',             # Operador de comparación
    r'>',             # Operador de comparación
    r'<=',            # Operador de comparación
    r'>=',            # Operador de comparación
    r'!=',            # Operador de comparación
    r'\.',            # Punto
    r',',             # Coma
    r';',             # Punto y coma
    r'"([^"]*)"',     # Cadena entre comillas dobles
    r"'([^']*)'",     # Cadena entre comillas simples
]

# Crear la expresión regular combinada para buscar los tokens
regex = '|'.join('(%s)' % token for token in tokens)

# Función para analizar la consulta
def analizar_consulta(consulta):
    matches = re.finditer(regex, consulta)
    for match in matches:
        for i, token in enumerate(tokens):
            if match.group(i + 1):
                print(f'Tipo: {token}, Valor: {match.group(i + 1)}')

# Ejemplo de uso
consulta = "SELECT * FROM usuarios WHERE edad > 18;"
analizar_consulta(consulta)

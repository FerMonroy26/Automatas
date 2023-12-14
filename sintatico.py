def tokenize_sql_query(query):
    # Mapeo de tokens
    token_mapping = {
        'SELECT': 333,
        'FROM': 245,
        ';': 12,
        ',': 23,
        # ... otros tokens
    }

    words = query.split()

    # Inicializar una lista para almacenar los tokens resultantes
    tokens = []

    # Asignar tokens a cada palabra en la consulta
    for word in words:
        token = token_mapping.get(word, word)
        tokens.append(token)

        # Agregar un salto de línea después de cada punto y coma
        if word == ';':
            tokens.append('\n')

    return tokens

# Ejemplo de uso
sql_query = "SELECT name, edad FROM tabla; SELECT other_column FROM other_table;"
resulting_tokens = tokenize_sql_query(sql_query)
print(resulting_tokens)

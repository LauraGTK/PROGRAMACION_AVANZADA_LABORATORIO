# Ejercicio 3 Palabras a remplaza y minusculas
"""La cadena de texto y la lista de palabras tienen valores predeterminados.
En la definición de la función le damos valor a la cadena de texto.
En python las listas son objetos mutables, se pueden modificar sobre la marcha, si la definimos ahora
se crearía la lista una sola vez"""

def process_text(text: str = "This is a default text with Python and amazing words.",
    words_to_replace: list[str] = None) -> tuple[str, int]:
    """Procesa una cadena convirtiéndola a minúsculas, eliminando espacios iniciales
    y finales, y sustituyendo las palabras que coinciden con las de la lisat por asteriscos.

    Parámetros:
        text (str): Texto a procesar.
        words_to_replace (list[str], opcional): Lista de palabras a
        reemplazar.

    Devuelve:
        tuple[str, int]: Texto modificado y número total de palabras
        reemplazadas.
    """

    if words_to_replace is None: #le damos el valor predeterminado a la lista
        words_to_replace = ["Python", "amazing"]
    """Tenemos en cuenta que:
    - .strip() elimina los espacios de los exremos
    - .lower() lo pasa todo a minúscula"""
    cleaned_text = text.strip().lower()
    # Convertir las palabras a reemplazar a minúsculas usando una lista (sin usar set)
    lower_words_to_replace = []
    for w in words_to_replace:
        lower_words_to_replace.append(w.lower())
    """.split --> divide toda la cadena por los espacios intermedios y la convierte en una lista de palabras individuales"""
    words = cleaned_text.split() 
    replaced_count = 0
    processed_words = []

    for word in words:
        """El if comprueba si la palabra actual está dentro de las que hay que reemplazar"""
        if word in lower_words_to_replace:
            """len(word) calcula las letras de la palabra para sustituirlas por asteriscos"""
            processed_words.append("*" * len(word))
            """Usamos replaced_count para contar el numero de palabras modificadas"""
            replaced_count += 1
        else:
            processed_words.append(word)
    """Juntamos las palabras en una cadena de texto"""
    result_text = " ".join(processed_words)
    return result_text, replaced_count


def main() -> None:
    """Prueba la función process_text con valores predeterminados y personalizados."""
    # Prueba con valores por defecto
    res_text, count = process_text()
    print(f'Processed text: "{res_text}"')
    print(f"Palabras reemplazadas: {count}")

    print("\n--- Prueba con valores personalizados ---")
    custom_text = (
        "Python is an AMAZING programming language. Python is popular."
    )
    custom_words = ["python", "amazing"]
    res_custom, count_custom = process_text(custom_text, custom_words)
    print(f'Processed text: "{res_custom}"')
    print(f"Palabras reemplazadas: {count_custom}")


if __name__ == "__main__":
    main()
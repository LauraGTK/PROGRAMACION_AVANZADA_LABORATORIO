# Ejercicio 5 Palíndromo, se lee igual de izquierda a derecha


def normalize(text: str) -> str:
    """Convierte el texto a minúsculas, elimina tildes/diéresis en vocales
    y conserva el resto en minúsculas

    Parámetros:
        text (str): Texto original

    Devuelve:
        str: Texto modificado y en minúscula
    """
    text = text.lower()         #pasamos a minúsculas

    """Añadimos todos los posibles cambios"""
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    text = text.replace("ü", "u")

    filtered_chars = []
    for char in text: 
        if char.isalnum():          #.isalnum() -> comprueba si los caracteres son alfanumericos (letras o numeros)
            filtered_chars.append(char)

    return "".join(filtered_chars)


def is_palindrome(text: str) -> bool:
    """Comprueba si un texto es un palíndromo ignorando espacios, puntuación y tildes

    Parámetros:
        text (str): Texto a verificar

    Devuelve:
        bool: True si es palíndromo, False en caso contrario
    """
    norm = normalize(text)          #normalize definida anteriormente
    """slicing -> [inicio:fin:paso], norm[::-1] le da la vuelta a la frase
    y return norm == norm[::-1] devuelve true si son iguales"""
    return norm == norm[::-1]       


def find_palindromes(sentences: list[str]) -> list[str]:
    """Filtra una lista de frases devolviendo únicamente las que son palíndromos

    Parámetros:
        sentences (list[str]): Lista de frases

    Devuelve:
        list[str]: Lista de frases palíndromas
    """
    return [s for s in sentences if is_palindrome(s)]


def palindrome_words(text: str) -> list[str]:
    """Devuelve la lista de palabras palíndromas de al menos 3 letras contenidas
    en la frase recibida (sin signos de puntuación)

    Parámetros:
        text (str): Frase a analizar

    Devuelve:
        list[str]: Lista de palabras palíndromas tal y como aparecen escritas
    """
    words = text.split()
    result = []
    for word in words:
        if len(word) >= 3 and is_palindrome(word):
            result.append(word)
    return result


def main() -> None:
    """Ejecuta las pruebas del ejercicio de palíndromos."""
    sentences = [
        "Anita lava la tina",
        "Dábale arroz a la zorra el abad",
        "Esto no es un palindromo",
        "¿Acaso hubo búhos acá?",
    ]

    print("--- Frases palíndromas encontradas ---")
    for phrase in find_palindromes(sentences):
        print(phrase)

    print("\n--- Palabras palíndromas (mínimo 3 letras) ---")
    test_phrase = "Ana vio un oso en el ojo de Anita"
    print(
        f"En '{test_phrase}':",
        palindrome_words(test_phrase),
    )


if __name__ == "__main__":
    main()
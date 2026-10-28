# Ejercicio 12


def is_anagram(word1: str, word2: str) -> bool:
    """
    Comprueba si dos palabras son anagramas.
    Ignora las mayúsculas, minúsculas y espacios.

    Parámetros:
        word1 (str): Primera frase o palabra.
        word2 (str): Segunda frase o palabra.

    Devuelve:
        bool: True si son anagramas y False en caso contrario.
    """

    #minusculas y espacios
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Ordenamos las letras y comparamos
    return sorted(word1) == sorted(word2)



def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Agrupa las palabras que son anagramas entre sí.

    Mantiene el orden en el que aparecen las palabras.

    Parámetros:
        words (list[str]): Lista de palabras.

    Devuelve:
        list[list[str]]: Lista de grupos de anagramas.
    """

    grupos = []


    for palabra in words:

        encontrado = False

        for grupo in grupos:

   
            if is_anagram(palabra, grupo[0]):

                grupo.append(palabra)

                encontrado = True
                break


        if not encontrado:
            grupos.append([palabra])

    return grupos



def largest_group(words: list[str]) -> list[str]:
    """
    Encuentra el grupo de anagramas con más palabras.
    En caso de empate, devuelve el primero.

    Parámetros:
        words (list[str]): Lista de palabras.

    Devuelve:
        list[str]: Grupo de anagramas más grande.
        Si no hay palabras, devuelve una lista vacía.
    """

    # Obtenemos los grupos de anagramas
    grupos = group_anagrams(words)


    if len(grupos) == 0:
        return []

    # Suponemos que el primer grupo es el más grande
    mayor = grupos[0]

    for grupo in grupos:

        if len(grupo) > len(mayor):
            mayor = grupo

    return mayor



def find_anagrams(word: str, words: list[str]) -> list[str]:
    """
    Busca los anagramas de una palabra dentro de una lista.
    Excluye la propia palabra, ignorando mayúsculas y minúsculas.

    Parámetros:
        word (str): Palabra de referencia.
        words (list[str]): Lista de palabras donde buscar.

    Devuelve:
        list[str]: Palabras que son anagramas de la palabra dada.
    """

    resultado = []

    for palabra in words:

        if is_anagram(word, palabra):

            # Evitamos incluir la propia palabra
            if word.lower() != palabra.lower():
                resultado.append(palabra)

    return resultado


def main() -> None:
    print("1. COMPROBAR ANAGRAMAS")

    print("¿amor y roma son anagramas?",
          is_anagram("amor", "roma"))

    print("¿hola y casa son anagramas?",
          is_anagram("hola", "casa"))

    print("¿Listen y Silent son anagramas?",
          is_anagram("Listen", "Silent"))

    palabras = [
        "amor",
        "roma",
        "perro",
        "mora",
        "gato",
        "toga",
        "casa"
    ]

    print("\n2. AGRUPAR ANAGRAMAS")

    print("Los grupos de anagramas son:")
    print(group_anagrams(palabras))

    print("\n3. GRUPO MÁS GRANDE")

    print("El grupo más grande es:")
    print(largest_group(palabras))

    print("\n4. BUSCAR ANAGRAMAS")

    print("Los anagramas de amor son:")
    print(find_anagrams("amor", palabras))

   
    print("\n5. LISTA VACÍA")

    print("Grupos:", group_anagrams([]))
    print("Grupo más grande:", largest_group([]))


if __name__ == "__main__":
    main()
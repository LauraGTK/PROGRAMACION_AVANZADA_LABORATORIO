# Ejercicio 10 Lee lista de cadenas, menú

def comenzar_por(cadenas: list[str], prefijo: str) -> list[str]:
    """
    Devuelve las cadenas que comienzan por un prefijo determinado.

    Parámetros:
        cadenas (list[str]): Lista de cadenas de texto.
        prefijo (str): Prefijo que queremos buscar.

    Devuelve:
        list[str]: Lista de cadenas que empiezan por el prefijo.
    """
    resultado = []

    for cadena in cadenas:
        if cadena.startswith(prefijo):
            resultado.append(cadena)

    return resultado



def contar_subcadena(cadenas: list[str], subcadena: str) -> int:
    """
    Cuenta cuántas cadenas contienen una subcadena determinada.

    Parámetros:
        cadenas (list[str]): Lista de cadenas de texto.
        subcadena (str): Texto que queremos buscar.

    Devuelve:
        int: Número de cadenas que contienen la subcadena.
    """
    contador = 0

    for cadena in cadenas:
        if subcadena in cadena:
            contador += 1

    return contador



def larga_corta(cadenas: list[str]) -> tuple[str, str] | None:
    """
    Encuentra la cadena más larga y la más corta de una lista.
    Si hay empate, se conserva la primera encontrada.

    Parámetros:
        cadenas (list[str]): Lista de cadenas de texto.

    Devuelve:
        tuple[str, str] | None: Cadena más larga y más corta,
        o None si la lista está vacía.
    """
    if len(cadenas) == 0:
        return None

    larga = cadenas[0]
    corta = cadenas[0]

    for cadena in cadenas:
        if len(cadena) > len(larga):
            larga = cadena

        if len(cadena) < len(corta):
            corta = cadena

    return larga, corta


def mismo_objeto(cadena1: str, cadena2: str) -> bool:
    """
    Comprueba si dos variables hacen referencia al mismo objeto.

    Parámetros:
        cadena1 (str): Primera cadena.
        cadena2 (str): Segunda cadena.

    Devuelve:
        bool: True si son el mismo objeto y False en caso contrario.
    """
    return cadena1 is cadena2


def hay_cadena_larga(cadenas: list[str]) -> bool:
    """
    Comprueba si alguna cadena tiene más de 10 caracteres
    Parámetros:
        cadenas (list[str]): Lista de cadenas de texto.

    Devuelve:
        bool: True si alguna cadena supera los 10 caracteres
        y False en caso contrario.
    """
    for cadena in cadenas:
        if len(cadena) > 10:
            break
    else:
        return False

    return True



def main() -> None:
    texto = input("Introduce cadenas separadas por comas: ")

    cadenas = texto.split(",")

    # Eliminamos los espacios al principio y al final de cada cadena
    cadenas = [cadena.strip() for cadena in cadenas]

    # Si no se introduce ningún texto, dejamos la lista vacía
    if texto.strip() == "":
        cadenas = []

    while True:

        print("\n--- MENÚ ---")
        print("1. Buscar cadenas que comienzan por un prefijo")
        print("2. Contar cadenas que contienen una subcadena")
        print("3. Encontrar la cadena más larga y la más corta")
        print("4. Comprobar si dos cadenas son el mismo objeto")
        print("5. Comprobar si hay cadenas de más de 10 caracteres")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            prefijo = input("Introduce el prefijo: ")
            resultado = comenzar_por(cadenas, prefijo)
            print("Las cadenas que comienzan por", prefijo, "son:", resultado)

        elif opcion == "2":
            subcadena = input("Introduce la subcadena: ")
            resultado = contar_subcadena(cadenas, subcadena)
            print("El número de cadenas que contienen", subcadena, "es:", resultado)

        elif opcion == "3":
            resultado = larga_corta(cadenas)

            if resultado is None:
                print("La lista está vacía.")
            else:
                larga, corta = resultado
                print("La cadena más larga es:", larga)
                print("La cadena más corta es:", corta)

        elif opcion == "4":
            if len(cadenas) < 2:
                print("Se necesitan al menos dos cadenas.")
            else:
                if mismo_objeto(cadenas[0], cadenas[1]):
                    print("Las dos primeras cadenas son el mismo objeto.")
                else:
                    print("Las dos primeras cadenas no son el mismo objeto.")

        elif opcion == "5":
            if hay_cadena_larga(cadenas):
                print("Hay al menos una cadena de más de 10 caracteres.")
            else:
                print("No hay ninguna cadena de más de 10 caracteres.")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
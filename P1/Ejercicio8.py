# Ejercicio 8 lee una lista de numeros y realiza distintas opciones elegidas por menu


def suma(numbers: list[int]) -> int:
    """Suma todos los números de una lista.

    Parámetros:
        numbers (list[int]): Lista de enteros.

    Devuelve:
        int: Suma total.
    """
    total = 0
    for n in numbers:
        total += n
    return total


def suma_pos_neg(numbers: list[int]) -> tuple[int, int]:
    """Calcula la suma de los números positivos y negativos por separado.

    Parámetros:
        numbers (list[int]): Lista de enteros.

    Devuelve:
        tuple[int, int]: (suma_positivos, suma_negativos)
    """
    positivos = 0
    negativos = 0
    for n in numbers:
        if n > 0:
            positivos += n
        elif n < 0:
            negativos += n
    return positivos, negativos


def max_min(numbers: list[int]) -> tuple[int, int] | None:
    """Encuentra el valor máximo y mínimo de la lista.

    Parámetros:
        numbers (list[int]): Lista de enteros.

    Devuelve:
        tuple[int, int] | None: Tupla (máximo, mínimo) o None si está vacía.
    """
    if not numbers:
        return None
    maximo = numbers[0]
    minimo= numbers[0]
    for n in numbers[1:]:
        if n > maximo:
            maximo = n
        if n < minimo:
            minimo = n
    return maximo, minimo

def comp_unicos(numbers: list[int]) -> bool:
    """Comprueba si todos los elementos de la lista son únicos (todos diferentes).

    Parámetros:
        numbers (list[int]): Lista de enteros.

    Devuelve:
        bool: True si todos los elementos son diferentes o la lista está vacía, False en caso contrario.
    """
    repetidos = []
    for n in numbers:
        if n in repetidos:
            return False
        else:
            repetidos.append(n)
    return True


def compara_pos_neg(numbers: list[int]) -> str:
    """Compara la cantidad de números positivos y negativos de una lista.

    Parámetros:
        numbers (list[int]): Lista de enteros.

    Devuelve:
        str: Mensaje descriptivo del resultado.
    """
    contador_positivos= 0
    contador_negativos = 0
    for n in numbers:
        if n > 0:
            contador_positivos += 1
        elif n < 0:
            contador_negativos += 1

    return (
        "La lista contiene más números positivos que negativos."
        if contador_positivos > contador_negativos
        else 
        (
            "La lista contiene más números negativos que positivos."
            if contador_negativos > contador_positivos
            else "La lista contiene la misma cantidad de números positivos y negativos."
        )
    )


def main() -> None:
    """Menú interactivo."""
    texto = input("Introduzca su lista de números enteros. Sepárelos con espacios: ")
    numeros = [int(n) for n in texto.split()]

    while True:
        print("\n---OPCIONES DE OPERACIÓN ---")
        print("\n1. Suma total")
        print("2. Suma de positivos y negativos")
        print("3. Máximo y mínimo")
        print("4. Comprobar si todos son únicos")
        print("5. Comparar cantidad de positivos y negativos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("La suma de todos los números es:", suma(numeros))

        elif opcion == "2":
            positivos, negativos = suma_pos_neg(numeros)
            print("La suma de los positivos es:", positivos)
            print("La suma de los negativos es:", negativos)

        elif opcion == "3":
            resultado = max_min(numeros)

            if resultado is None:
                print("La lista está vacía.")
            else:
                maximo, minimo = resultado
                print("El número máximo es:", maximo)
                print("El número mínimo es:", minimo)

        elif opcion == "4":
            if comp_unicos(numeros):
                print("Todos los números de la lista son únicos.")
            else:
                print("Hay números repetidos en la lista.")

        elif opcion == "5":
            print(compara_pos_neg(numeros))

        elif opcion == "6":
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    main()
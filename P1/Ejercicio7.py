# Ejercicio 7 funciones sobre listas de numeros sin hacer uso de sorted(), list.sort(), set() ni el módulo statistics


def remove_duplicates(numbers: list[int]) -> list[int]:
    """Devuelve una nueva lista sin duplicados conservando el orden de la primera aparición

    Parámetros:
        numbers (list[int]): Lista de números enteros

    Devuelve:
        list[int]: Lista sin duplicados
    """
    unique_list = []
    for num in numbers:
        if num not in unique_list:  #si no aparece lo almaceno
            unique_list.append(num)
    return unique_list


def rotate_left(numbers: list[int], k: int) -> list[int]:
    """Rota los elementos de una lista k posiciones hacia la izquierda

    Parámetros:
        numbers (list[int]): Lista de enteros
        k (int): Desplazamiento hacia la izquierda

    Devuelve:
        list[int]: Nueva lista rotada
    """
    if not numbers:
        return []
    n = len(numbers)
    k = k % n
    res = []
    for i in range(n):
        """Busca qué elemento de la lista original debe colocarse en la nueva posición i
        Le suma k al índice actual i para avanzar k pasos. Al aplicar % n, si el resultado supera 
        la longitud de la lista, vuelve automáticamente al principio (posición 0)"""
        res.append(numbers[(i + k) % n]) 
    return res


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Separa los números pares e impares en dos listas independientes respetando el orden

    Parámetros:
        numbers (list[int]): Lista de enteros

    Devuelve:
        tuple[list[int], list[int]]: Tupla de listas (pares, impares)
    """
    pares = []
    impares = []
    for num in numbers:
        if num % 2 == 0:            #Comprobamos si son pares, buscando si el resto de la división entera por 2 es 0
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Combina dos listas previamente ordenadas de menor a mayor en una sola lista ordenada

    Parámetros (ambas listas):
        a (list[int]): Primera lista ordenada
        b (list[int]): Segunda lista ordenada

    Devuelve:
        list[int]: Lista combinada y ordenada
    """
    merged = []        #Creamos una lista vacía
    """Inicializamos dos variables con valor 0"""
    i = 0
    j = 0
    while i < len(a) and j < len(b):   #Nos mantenemos, en el bucle, dentro de la longitud de las listas
        if a[i] <= b[j]:               #Si el valor del número de la primera lista es menor, lo almacenamos en la lista vacía que hemos creado
            merged.append(a[i])
            i += 1                     #Comparamos el segundo numero de la lista a con el primero de b, y continúamos el bucle
        else:
            merged.append(b[j])
            j += 1
    """En caso de que una lista sea más larga que otra, añadimos dos bucles while para terminar de recorrer
    dichas listas. Y nos aseguramos de que van de menor a mayor porque ambas listas han sido ordenadas previamente"""
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged


def second_largest(numbers: list[int]) -> int | None:
    """Devuelve el segundo valor más grande distinto del máximo recorriendo la lista una sola vez
       En el caso de quyue la lista esté vacía, todos sus elementos sean iguales o tenga un solo elemento
       la función devolverá NONE
    Parámetros:
        numbers (list[int]): Lista de enteros

    Devuelve:
        int | None: El segundo mayor   OR    None si no existe
    """
    max1 = None
    max2 = None
    for num in numbers:
        if max1 is None or num > max1:   #max1 is None para la primera iteración y or para el resto
            max2 = max1
            max1 = num
            """Con num != max1 nos aseguramos de que el número a evaluar no sea repetido del máximo
            Ahora, max2 is None por si el valor de max2 no se ha modificado, y or num > max2 en caso
            de tener un valor guardado"""
        elif num != max1 and (max2 is None or num > max2):
            max2 = num
    return max2


def main() -> None:
    """Realizamos una prueba de las operaciones sobre listas del Ejercicio 7, con los ejemplos proporcionados"""
    print("remove_duplicates([3, 1, 3, 2, 1]):", remove_duplicates([3, 1, 3, 2, 1]))
    print("rotate_left([1, 2, 3, 4, 5], 2):", rotate_left([1, 2, 3, 4, 5], 2))
    print("rotate_left([1, 2, 3, 4, 5], 7):", rotate_left([1, 2, 3, 4, 5], 7))
    print("rotate_left([1, 2, 3, 4, 5], -1):", rotate_left([1, 2, 3, 4, 5], -1))
    print("rotate_left([1, 2, 3, 4, 5], 0):", rotate_left([1, 2, 3, 4, 5], 0))
    print("split_even_odd([1, 2, 3, 4, 5, 6]):", split_even_odd([1, 2, 3, 4, 5, 6]))
    print("merge_sorted([1, 4, 9], [2, 3, 10, 11]):", merge_sorted([1, 4, 9], [2, 3, 10, 11]))
    print("second_largest([4, 9, 2, 9, 7]):", second_largest([4, 9, 2, 9, 7]))
    print("second_largest([5, 5]):", second_largest([5, 5]))


if __name__ == "__main__":
    main()
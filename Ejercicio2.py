#Ejercicio 2 calendario gregoriano
def is_leap_year(year: int) -> bool:
    """Recibe un numero y determina si ees bisiesto (mediante el calendario gregoriano).
    
    Parámetros:
        year (int): El año a evaluar.

    Devuelve:
        bool: True si el año es bisiesto, False si no.
    """
    """Utilizamos el operador % para calcular el resto de una división entera.
       Para que sea bisiesto:
           - Divisible entre 4
           - Si es divisible por 100 NO es bisiesto
           - Si es divisible por 400 SI es bisiesto """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def leap_years_between(start: int, end: int) -> list[int]:
    """Devuelve la lista de años bisietos comprendidos entre start y end

    Parámetros:
        start(int): Año inicial
        end(int): Año final

    Devuelve:
        list[int]: Lista de años bisiestos comprendidos entre el año de inicio y el final
    """
    """Inicializamos una lista vacía"""
    leap_years = []
    """En el rango ponemos end + 1 para que end también calcule el último año.
    No es necesario inicializar year, el bucle for lo hace de manera automática"""
    for year in range(start, end + 1): # la funcion range(inicio, fin) tiene un incremento de 1
        if is_leap_year(year):
            leap_years.append(year) #append va añadiendo elemento a la lista
    return leap_years

def explain_leap_year (year: int)-> str:
    """Devuelve una cadena explicando por qué un año es o no bisiesto.

    Parámetros:
        year (int): Año a evaluar.

    Devuelve una cadena:
        str: Explicación textual del estado del año.
    """ 
    if year % 400 == 0:
        return f"{year} es bisiesto: es divisible entre 400."
    elif year % 100 == 0:
        return f"{year} no es bisiesto: es divisible entre 100 pero no entre 400."
    elif year % 4 == 0:
        return f"{year} es bisiesto: es divisible entre 4 y no entre 100."
    else:
        return f"{year} no es bisiesto: no es divisible entre 4."


def main() -> None:
    """Función principal para probar la lógica de años bisiestos."""
    years_to_test = [1900, 2000, 2023, 2024, 1500]
    for year in years_to_test:
        print(f"Año: {year}")
        if year < 1582:
            print("El calendario gregoriano se estableció en 1582.")
        else:
            print(explain_leap_year(year))
        print()

    print("Ejemplo de uso de leap_years_between(1896, 1912):")
    print(leap_years_between(1896, 1912)) 

if __name__ == "__main__":
    main()
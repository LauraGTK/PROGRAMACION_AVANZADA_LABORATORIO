#Ejercicio 1 segundos a dias, horas, minutos y segundos
def is_integer(text: str) -> bool:
    """Recibe una cadena y devuelve True si representa un número entero
    (positivo, negativo o cero) y False en caso contrario.

    Parámetros:
        text (str): La cadena a evaluar.

    Devuelve:
        bool: True si la cadena se puede convertir a int, False si no.
    """
    try:
        """Interpreta el contenido de la variable text y convertirlo en un número entero
        try evalua si la conversión es posible"""
        int(text)
        return True
    except ValueError:
        return False


def seconds_to_dhms(total_seconds: int) -> tuple[int, int, int, int]:
    """Convierte un número entero no negativo de segundos en días, horas,
    minutos y segundos.

    Parámetros:
        total_seconds (int): Segundos totales a descomponer.

    Devuelve:
        tuple[int, int, int, int]: Tupla (listado de datos) en el formato (días, horas, minutos,
        segundos).
    """
    dias = total_seconds // 86400
    resto = total_seconds % 86400
    horas = resto // 3600
    resto %= 3600
    minutos = resto // 60
    segundos = resto % 60
    return dias, horas, minutos, segundos


def main() -> None:
    """Función principal.
    Solicita al usuario una cantidad de segundos hasta obtener un entero no
    negativo y muestra la descomposición en días, horas, minutos y segundos.
    """
    while True:
        user_input = input("Introduzca los segundos: ")
        if is_integer(user_input):
            segundos = int(user_input)
            """Comprobamos que la entrada es un numero positivo"""
            if segundos >= 0:
                break
        print("Entrada no válida. Introduzca un entero no negativo.")

    d, h, m, s = seconds_to_dhms(segundos)
    """Añadimos la f dentro de print ya que así podemos incrustar variables directamente
    dentro de una cadena de texto"""
    print(f"{segundos} segundos son {d} d, {h} h, {m} min y {s} s.")


if __name__ == "__main__":
    main()
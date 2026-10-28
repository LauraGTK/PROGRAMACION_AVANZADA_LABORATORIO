# Ejercicio 9 funciones de polinomios y monomios 

def format_monomial(coef: int | float, exp: int) -> str:
    """Inicializa un monomio con su signo explícito siguiendo las reglas del enunciado.
    El índice de la lista es el exponente y el valor almacenado el coeficiente
    Parámetros:
        coef (float | int): Coeficiente del término.
        exp (int): Exponente del término.

    Devuelve:
        str: Monomio formateado con signo explícito.
    """
    if coef == 0:
        return ""

    """Añadir expresamente el +"""
    signo = "+" if coef > 0 else "-"

    if exp == 0:
        return signo + str(abs(coef))

    if abs(coef) == 1:
        termino = "x"
    else:
        termino = str(abs(coef)) + "x"

    if exp > 1:
        termino += "**" + str(exp)

    return signo + termino


def format_polynomial(coefs: list[int | float]) -> str:
    """Devuelve el polinomio como una cadena.

    Parámetros:
        coefs (list[float | int]): Coeficientes indicando el exponente por su posición.

    Devuelve:
        str: Representación en cadena del polinomio.
    """

    resultado = ""
    """Recorrer la lista desde ultimo a primero"""
    for exp in range(len(coefs) - 1, -1, -1):
        termino = format_monomial(coefs[exp], exp)

        if termino != "":
            if resultado == "":
                resultado = termino
            else:
                resultado += " " + termino[0] + " " + termino[1:]

    if resultado == "":
        return "0"

    if resultado[0] == "+":
        resultado = resultado[1:]

    return resultado


def evaluate(coefs: list[int | float], x: int | float) -> int | float:
    """Evalúa el polinomio para un valor dado de x.

    Parámetros:
        coefs (list[float | int]): Coeficientes del polinomio.
        x (float | int): Valor en el que evaluar.

    Devuelve:
        float: Resultado numérico de la evaluación.
    """
    resultado = 0

    for exp in range(len(coefs)):
        resultado += coefs[exp] * x ** exp

    return resultado


def derivative(coefs: list[float | int]) -> list[float | int]:
    """Calcula la derivada del polinomio.

    Parámetros:
        coefs (list[float | int]): Coeficientes del polinomio original.

    Devuelve:
        list[float | int]: Coeficientes del polinomio derivado.
    """
    resultado = []

    for exp in range(1, len(coefs)):
        resultado.append(coefs[exp] * exp)

    return resultado


def main() -> None:
    """Prueba el formateo, evaluación y derivación de polinomios."""
    coefs = [4.0, 1.0, 0.0, 2.0]

    print(format_monomial(2.0, 3))
    print(format_polynomial(coefs))
    print(evaluate(coefs, 2))
    print(derivative(coefs))

    print(format_polynomial([0.0, -1.0, 3.0]))
    print(format_polynomial([]))


if __name__ == "__main__":
    main()
# Ejercicio 6 Análisis de números primos


def is_prime(n: int) -> bool:
    """Comprueba si un número entero n es primo, los números menores de 2 no lo son

    Parámetros:
        n (int): Número entero a evaluar

    Devuelve:
        bool: True si es primo, False en caso contrario
    """
    if n < 2:
        return False
    # Probamos todos los números desde el 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False  # Si se puede dividir de forma exacta por alguno, no es primo
            
    return True  

def prime_list(limit: int) -> list[int]:
    """Genera una lista de números primos hasta el límite indicado

    Parámetros:
        limit (int): Límite 

    Devuelve:
        list[int]: Lista de números primos
    """
    if limit < 2:
        return []
    return [num for num in range(2, limit + 1) if is_prime(num)] #añadimos en range limit + 1 ya que queremos que haga hasta ese limite incluido


def check_palindrome(primes: list[int]) -> list[int]:
    """Busca y devuelve los números primos que son palíndromos

    Parámetros:
        primes (list[int]): Lista de números primos

    Devuelve:
        list[int]: Lista de primos palíndromos
    """
    palindromes = []
    for p in primes:
        s = str(p)
        if s == s[::-1]:
            palindromes.append(p)
    return palindromes


def categorize_prime(prime: int) -> str:
    """Clasifica un número primo según su tamaño

    Parámetros:
        prime (int): Número primo

    Devuelve:
        str: 'pequeño', 'mediano' o 'grande'
    """
    if prime < 10:
        return "pequeño"
    elif prime < 100:
        return "mediano"
    else:
        return "grande"


def main() -> None:
    """Prueba el análisis de números primos."""
    limit = 106
    primes = prime_list(limit)
    print(f"Primos hasta {limit}: {primes}\n")

    palindromic_primes = check_palindrome(primes)
    print(f"Primos palíndromos hasta {limit}: {palindromic_primes}\n")

    print("Clasificación de algunos primos:")
    for p in [1, 2, 13, 22, 101]:
        print(f"El primo {p} es {categorize_prime(p)}.")


if __name__ == "__main__":
    main()
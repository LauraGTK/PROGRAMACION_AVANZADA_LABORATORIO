# Ejercicio 4 cifrado César


def shift_char(char: str, shift: int) -> str:
    """Desplaza un carácter alfabético 'shift' posiciones (introducidas por el usuario) dentro del alfabeto inglés a-z

    Mantiene el las mayúsculas y el resto de caracteres, es decir solo se ven afectadas las minúsculas

    Parámetros:
        char (str): Carácter a desplazar
        shift (int): Número de posiciones de desplazamiento

    Devuelve:
        str: Carácter nodificado
    """
    if "a" <= char <= "z":                                          #si el carácter se encuentra denro del abecedario ingles
        base = ord("a")                                             #ord() -> re4ecibe una cadena de un caracter y devuelve su codigo numerico, en este caso de a
        """Si char es 'c' y base es 'a': ord('c') - ord('a') es 99 - 97 = 2. La 'c' es la letra en la posición 2 del alfabeto (desde 0)
            hacemos + shift para que tome la posicion que buscamos
            %26 es el resto entero, para que si llega a z (27)"le de la vuelta" al alfabeto
            + base, para saber que valor toma y poder traducirlo con chr"""
        return chr((ord(char) - base + shift) % 26 + base)
    
    elif "A" <= char <= "Z":                            #en caso de las mayusculas, realizamos lo mismo
        base = ord("A")
        return chr((ord(char) - base + shift) % 26 + base)
    return char


def encrypt(text: str, shift: int) -> str:
    """Cifra un texto utilizando el cifrado César con un desplazamiento dado

    Parámetros:
        text (str): Texto sin cifar
        shift (int): Desplazamiento

    Devuelve:
        str: Texto cifrado
    """

    return "".join(shift_char(c, shift) for c in text)


def decrypt(text: str, shift: int) -> str:
    """Descifra un texto cifrado previamente con el algoritmo César

    Parámetros:
        text (str): Texto cifrado
        shift (int): Desplazamiento

    Devuelve:
        str: Texto descifrado.
    """
    return encrypt(text, -shift)    #basta con tomar el valor opuesto del encriptado


def brute_force(cipher_text: str) -> list[str]:
    """Genera los 26 posibles descifrados de un texto cifrado

    Parámetros:
        cipher_text (str): Texto cifrado

    Devuelve:
        list[str]: Lista de 26 cadenas descifradas
    """
    return [decrypt(cipher_text, s) for s in range(26)]

"""Tomando los valores del ejemplo propuesto de la práctica"""
def main() -> None:
    """Prueba las funciones del cifrado César:"""
    print('encrypt("Hola, Mundo!", 3) ->', repr(encrypt("Hola, Mundo!", 3)))
    print(
        'decrypt("Krod, Pxqgr!", 3) ->', repr(decrypt("Krod, Pxqgr!", 3))
    )
    print('encrypt("xyz", 3) ->', repr(encrypt("xyz", 3)))
    print('encrypt("abc", -3) ->', repr(encrypt("abc", -3)))
    print(
        'brute_force("Krod, Pxqgr!")[3] ->',
        repr(brute_force("Krod, Pxqgr!")[3]),
    )


if __name__ == "__main__":
    main()
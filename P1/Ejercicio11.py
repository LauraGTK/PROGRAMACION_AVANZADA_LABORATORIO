#Ejercicio 11 informe pacientes hospital
import re
from datetime import datetime


def calcular_edad(nacimiento: str, consulta: str) -> int:
    """
    Calcula la edad del paciente en la fecha de consulta.

    Parámetros:
        nacimiento (str): Fecha de nacimiento del paciente.
        consulta (str): Fecha en la que se realiza la consulta.

    Devuelve:
        int: Edad del paciente en la fecha de consulta.
    """

    # Convertimos las fechas de texto a objetos datetime
    fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y")
    fecha_consulta = datetime.strptime(consulta, "%d/%m/%Y")


    edad = fecha_consulta.year - fecha_nacimiento.year

    # Comprobamos si el paciente ya ha cumplido años
    if (fecha_consulta.month, fecha_consulta.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad




def informe_anonimo(informe: str) -> str:
    """
    Anonimiza un informe médico eliminando los datos personales.

    Sustituye el nombre del paciente, el nombre del médico
    y las fechas. También calcula la edad del paciente.

    Parámetros:
        informe (str): Informe médico original.

    Devuelve:
        str: Informe médico con los datos anonimizados.
    """

    # Encontrar fechas con formato dd/mm/aaaa
    patron_fechas = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")

    # Buscamos todas las fechas del informe
    fechas = patron_fechas.findall(informe)

    # Comprobamos que tenemos al menos dos fechas
    if len(fechas) >= 2:


        nacimiento = fechas[0]
        consulta = fechas[1]


        edad = calcular_edad(nacimiento, consulta)

        # Sustituimos la fecha nacimiento por la edad
        informe = re.sub(
            r"Fecha de nacimiento:\s*\d{1,2}/\d{1,2}/\d{4}",
            f"Edad: {edad}",
            informe
        )

    # Sustituimos el nombre del paciente
    informe = re.sub(
        r"Paciente:[^\n]*",
        "Paciente: PACIENTE",
        informe
    )

    # Sustituimos el nombre del médico
    informe = re.sub(
        r"Médico:\s*(?:Dr|Dra)\.[^\n]*",
        "Médico: MEDICO",
        informe
    )

    # Sustituimos las fechas restantes
    informe = patron_fechas.sub("FECHA", informe)

    return informe


# FUNCIÓN PRINCIPAL

def main() -> None:

    informe1 = """nforme clínico de Urgencias
Nombre: Juan Pérez López
Género: Hombre
Fecha de nacimiento: 12/05/1980
Motivo de consulta: dolor abdominal
12/05/2023 Dr. Ramírez
Tratamiento: reposo y analgésicos"""


    print("INFORME ORIGINAL:")
    print(informe1)

    print("\nINFORME ANONIMIZADO:")
    print(informe_anonimo(informe1))


if __name__ == "__main__":
    main()
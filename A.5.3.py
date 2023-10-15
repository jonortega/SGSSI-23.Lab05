import hashlib
import re

def calcular_sha256(nombre_archivo):
    sha256 = hashlib.sha256()

    try:
        with open(nombre_archivo, "rb") as archivo:
            while True:
                data = archivo.read(65536)  # Leer en bloques de 64 KB
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def comprobar_archivos(archivo1, archivo2):
    try:
        with open(archivo1, "r") as file1, open(archivo2, "r") as file2:
            contenido1 = file1.read()
            contenido2 = file2.read()

        resumen_sha256_1 = calcular_sha256(archivo1)
        resumen_sha256_2 = calcular_sha256(archivo2)

        cumple_condicion = contenido2.startswith(contenido1) and \
                           bool(re.search(r'[0-9a-f]{8}\tfe\t100$', contenido2)) and \
                           bool(re.match(r'^0+', resumen_sha256_2))

        # print(f"({contenido2.startswith(contenido1)}, {bool(re.search(r'[0-9a-f]{8}\tfe\t100$', contenido2))}, {bool(re.match(r'^0+', resumen_sha256_2))})")
        return cumple_condicion

    except FileNotFoundError:
        print("Al menos uno de los archivos no se encontró.")

if __name__ == "__main__":
    # archivo1 = input("Ingrese el nombre del primer archivo de texto: ")
    # archivo2 = input("Ingrese el nombre del segundo archivo de texto: ")
    archivo1 = "SGSSI-23.CB.02.txt"
    archivo2 = "Output.txt"

    resultado = comprobar_archivos(archivo1, archivo2)
    print(f"Los ficheros cumplen las condiciones: {resultado}")

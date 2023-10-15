import hashlib

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
        # Leer el contenido completo de ambos archivos
        with open(archivo1, "r") as file1, open(archivo2, "r") as file2:
            contenido1 = file1.read()
            contenido2 = file2.read()

        # Calcular el resumen SHA-256 del archivo1
        resumen_sha256_1 = calcular_sha256(archivo1)
        resumen_sha256_2 = calcular_sha256(archivo2)

        cumple_condicion = (contenido1.startswith(contenido2) and f"{resumen_sha256_2}" in contenido1) or \
                           (contenido2.startswith(contenido1) and f"{resumen_sha256_1}" in contenido2)

        if cumple_condicion:
            return True
        else:
            return False
    except FileNotFoundError:
        print("Al menos uno de los archivos no se encontró.")

if __name__ == "__main__":
    archivo1 = input("Ingrese el nombre del primer archivo de texto: ")
    archivo2 = input("Ingrese el nombre del segundo archivo de texto: ")
    resultado = comprobar_archivos(archivo1, archivo2)
    print(f"Los ficheros cumplen las condiciones: {resultado}")

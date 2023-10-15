import hashlib
import time

def calcular_sha256(nombre_fichero):
    sha256 = hashlib.sha256()
    with open(nombre_fichero, "rb") as archivo:
        while True:
            datos = archivo.read(65536)  # Leer 64KB a la vez
            if not datos:
                break
            sha256.update(datos)
    return sha256.hexdigest()

def reescribir_fichero(nombre_fichero_entrada, nombre_fichero_salida):
    # Leer el contenido del fichero de entrada
    with open(nombre_fichero_entrada, "r") as entrada:
        contenido = entrada.read()

    with open(nombre_fichero_salida, "w") as salida:
        salida.write(contenido)

def escribir_nuevo_fichero_con_linea_final(nombre_fichero_entrada, nombre_fichero_salida, hex_adecuado):
    reescribir_fichero(nombre_archivo_entrada, nombre_archivo_salida)
    
    # Agregar la línea adicional
    with open(nombre_archivo_salida, "a") as salida:
        linea_adicional = f"{hex_adecuado}\tfe\t100\n"
        salida.write(linea_adicional)

def encontrar_hex_sha256(nombre_fichero_entrada, nombre_fichero_salida):
    valor_hex = "00000000" # Generar un valor hexadecimal inicial
    timeout = time.time() + 60 # Dentro de 60 segundos
    contador = 0
    while True:
        if time.time() > timeout:
            reescribir_fichero(nombre_fichero_entrada, nombre_fichero_salida)
            print("===TIEMPO LIMITE (60s) ALCANZADO===")
            print(f"Iteraciones calculadas: {contador}")
            exit(1)

        sha256 = calcular_sha256(nombre_fichero_salida)
        print(f"SHA-256 Output.txt: {sha256}")

        if sha256.startswith("00"):
            break

        valor_hex = format(int(valor_hex, 16) + contador, "08x")
        print(f"Valor HEX_8 calculado: {valor_hex}")
        escribir_nuevo_fichero_con_linea_final(nombre_fichero_entrada, nombre_fichero_salida, valor_hex)
        contador += 1

    return valor_hex

def crear_fichero_salida(nombre_fichero_entrada, nombre_fichero_salida):
    open(nombre_archivo_salida, "w") # Crear el fichero de salida vacio
    hex_adecuado = encontrar_hex_sha256(nombre_fichero_entrada, nombre_fichero_salida)

if __name__ == "__main__":
    # nombre_archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    # nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    nombre_archivo_entrada = "SGSSI-23.CB.02.txt"
    nombre_archivo_salida = "Output.txt"
    
    start = time.time()
    crear_fichero_salida(nombre_archivo_entrada, nombre_archivo_salida)
    end = time.time()
    
    print(f"Elapsed time: {round(end-start, 6)}s")
    print("Fichero de salida creado con exito.")

import sys
import os

config = {}

# Detecta automáticamente la carpeta exacta donde está guardado este script
dir_actual = os.path.dirname(os.path.abspath(__file__))
ruta_config = os.path.join(dir_actual, "config.txt")
ruta_output = os.path.join(dir_actual, "mandelbrot.csv")

# CASO 2: Manejo de error si no existe el archivo config.txt
try:
    with open(ruta_config, "r") as file:
        for line in file:
            # CASO 3: Manejo de error si una línea no contiene el formato 'parámetro=valor'
            try:
                parameter, value = line.strip().split("=")
                config[parameter] = float(value) if "." in value else int(value)
            except ValueError:
                print("El archivo de configuración está mal formado.")
                sys.exit(1)
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    sys.exit(1)

# CASO 4 y CASO 5: Validación de llaves existentes y tipos de datos correctos
try:
    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]
    
    # CASO 5: Validación explícita de que ancho y alto sean enteros
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError
        
    real_min = config["real_min"]
    real_max = config["real_max"]
    imag_min = config["imag_min"]
    imag_max = config["imag_max"]

except KeyError as e:
    print(f"Falta el parámetro {e} en config.txt.")
    sys.exit(1)
except TypeError:
    print("ancho y alto deben ser números enteros.")
    sys.exit(1)

# Procesamiento y escritura del archivo de salida (Caso 1)
with open(ruta_output, "w") as output:
    output.write("row,column,iterations\n")

    for row in range(height):
        for column in range(width):
            real = real_min + (column / width) * (real_max - real_min)
            imag = imag_min + (row / height) * (imag_max - imag_min)
            c = complex(real, imag)
            
            z = 0 + 0j
            iterations = 0
            
            while (abs(z) <= 2) and (iterations < max_iter):
                z = z * z + c
                iterations += 1
            
            output.write(f"{row},{column},{iterations}\n")
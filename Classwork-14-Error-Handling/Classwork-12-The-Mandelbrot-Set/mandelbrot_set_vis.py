import sys
import os
from PIL import Image

config = {}

dir_actual = os.path.dirname(os.path.abspath(__file__))
ruta_config = os.path.join(dir_actual, "config.txt")
ruta_csv = os.path.join(dir_actual, "mandelbrot.csv")

# CASO 2: si no existe el archivo config.txt
try:
    with open(ruta_config, "r") as file:
        lines = file.readlines()
        for line in lines:
            parameter, value = line.strip().split('=')
            config[parameter] = float(value) if '.' in value else int(value)
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    sys.exit(1)

# CASO 3:si no existe el archivo mandelbrot.csv
try:
    with open(ruta_csv, "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print("No se encontró el archivo mandelbrot.csv")
    sys.exit(1)

# No olvidar quitar los encabezados
lineas.pop(0)

# Desempaquetar variables
max_iter = config['max_iter']
ancho, alto = config['ancho'], config['alto']

img = Image.new('RGB', (ancho, alto)) 

for linea in lineas:
    # CASO 5: si una fila del csv está mal formada o tiene columnas de más
    try:
        valores = linea.strip().split(',')
        if len(valores) != 3:
            raise ValueError
        row, column, iterations = valores
        iterations = int(iterations)
        row = int(row)
        column = int(column)
    except ValueError:
        print("El archivo csv está mal formado.")
        sys.exit(1)

    # CASO 4: si una coordenada está fuera del tamaño de la imagen
    try:
        if iterations == max_iter:
            r, g, b = 0, 0, 0
        else:
            if max_iter > 500:
                r = (iterations * 15) % 256
                g = (iterations * 7) % 256
                b = (iterations * 2) % 256
            else:
                brillo = int((iterations / max_iter) * 255)
                r, g, b = brillo, brillo, brillo

        img.putpixel((column, row), (r, g, b))
    except IndexError:
        print("El csv no es consistente con el ancho/alto del config.txt.")
        sys.exit(1)

img_rgb = img.convert('RGB')

ruta_png = os.path.join(dir_actual, 'hipocampos.png' if max_iter > 500 else 'mandelbrot.png')
img_rgb.save(ruta_png) 
print('DONE')
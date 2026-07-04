from PIL import Image

config = {}

file = open("Classwork-11-The-Mandelbrot-Set/config.txt", "r")
lines = file.readlines()
for line in lines:
    parameter, value = line.strip().split('=')
    config[parameter] = float(value) if '.' in value else int(value)
file.close()

print(config)

archivo = open("Classwork-11-The-Mandelbrot-Set/mandelbrot.csv", "r")
lineas = archivo.readlines()
archivo.close()

#No olvidar quitar los encabezados
lineas.pop(0)

#Desempaquetar variables
max_iter = config['max_iter']
ancho, alto = config['ancho'], config['alto']

img = Image.new('RGB', (ancho, alto)) 

for linea in lineas:
    row, column, iterations = linea.strip().split(',')
    iterations = int(iterations)
    row = int(row)
    column = int(column)

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

img_rgb = img.convert('RGB')

img_rgb.save('hipocampos.png' if max_iter > 500 else 'mandelbrot.png') 
print('DONE')
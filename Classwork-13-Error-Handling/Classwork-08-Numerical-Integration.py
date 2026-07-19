import math
import sys

# INPUT

# CASO 8: validar que el límite inferior sea numérico
try:
    a_input = input("Write the left endpoint of the interval:")
    a = float(eval(a_input.replace("pi", "math.pi")))
except (ValueError, NameError, SyntaxError):
    print("El límite inferior debe ser numérico")
    sys.exit(1)

# CASO 9: validar que el límite superior sea numérico
try:
    b_input = input("Write the right endpoint of the interval:")
    b = float(eval(b_input.replace("pi", "math.pi")))
except (ValueError, NameError, SyntaxError):
    print("El límite superior debe ser numérico")
    sys.exit(1)

f_x = input("Write the function to integrate:")
method = input("Select the Integration Method (LRM/RRM/MPM/TRM):")

# PROCESS

# CASO 14: validar que los intervalos estén en el orden correcto
if a >= b:
    print("El límite inferior debe ser menor que el límite superior")
    sys.exit(1)

# CASO 15: validar que el método de integración seleccionado sea válido
if method not in ["LRM", "RRM", "MPM", "TRM"]:
    print("El método de integración no es válido. Usa LRM, RRM, MPM o TRM")
    sys.exit(1)

area=0.0
n=1000
h=(b-a)/n
shift=0
constant=0

if method=="RRM":
    shift=1
elif method=="MPM":
    constant=h/2
else:
    pass

# evaluar la función y ver si hay fallas matemáticas o de formato
try:
    if method=="TRM":
        f_x0 = eval(f_x, {"math": math, "x": a})
        f_x1 = eval(f_x, {"math": math, "x": b})

        sum_inter=0.0
        for i in range (1, n):
            xi= a+i*h
            sum_inter += eval(f_x, {"math": math, "x": xi})

        area = (h / 2) * (f_x0 + 2 * sum_inter + f_x1)
    else:
        for i in range (0 + shift, n + shift):
            xi= a+i*h + constant
            height = eval(f_x, {"math": math, "x": xi})
            area+= height*h
            
except ZeroDivisionError:
    # CASO 13: division entre cero dentro del intervalo
    print("La función no está definida en algún punto del intervalo")
    sys.exit(1)
except NameError:
    # CASO 11: variables diferentes a 'x'
    print("La función debe estar escrita en términos de x")
    sys.exit(1)
except SyntaxError:
    # CASO 10 y 12: Texto vacío o uso incorrecto de operadores
    print("La función ingresada no es válida")
    sys.exit(1)
        
# OUTPUT
print(f"The integration of {f_x} is {area:.3f}")
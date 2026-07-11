import math

#INPUT
a_input = input("Write the left endpoint of the interval:")
a = float(eval(a_input.replace("pi", "math.pi")))

b_input = input("Write the right endpoint of the interval:")
b = float(eval(b_input.replace("pi", "math.pi")))

f_x = input("Write the function to integrate:")
method = input("Select the Integration Method (LRM/RRM/MPM/TRM):")

#PROCESS
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
        
#OUTPUT
print(f"The integration of {f_x} is {area:.2f}")
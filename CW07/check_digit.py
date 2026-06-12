def get_check_digit(rol):
    
    clean_rol=rol.split('-')[0]
    reversed_rol=clean_rol[::-1]
    
    total_sum= 0
    multiplier= 2
    
    for digit in reversed_rol:
        total_sum+= int(digit) * multiplier
        multiplier+= 1
        if multiplier> 7:
            multiplier= 2

    remainder= total_sum%11
    result= 11-remainder

    if result==11:
        return '0'
    elif result==10:
        return 'K'
    else:
        return str(result)

user_input=input("Enter the UTFSM rol: ")
check_digit=get_check_digit(user_input)

print(f"The check digit is: {check_digit}")
print(f"Complete Rol: {user_input.split('-')[0]}-{check_digit}")


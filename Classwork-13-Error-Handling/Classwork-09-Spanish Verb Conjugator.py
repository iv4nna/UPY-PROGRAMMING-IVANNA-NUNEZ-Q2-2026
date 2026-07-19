import sys

pronouns=["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]

endings={
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"]
    }

# INPUT
verb=input("Write a spanish verb(ar/er/ir): ")

# CASO 24 Validar si contiene espacios extra
if verb != verb.strip():
    print("El verbo no debe tener espacios extra")
    sys.exit(1)

# CASO 23 Validar estrictamente si contiene letras mayúsculas
if any(char.isupper() for char in verb):
    print("El verbo debe escribirse en minúsculas")
    sys.exit(1)

# CASO 19 20 21 y 22 Errores de terminación o textos inválidos
try:
    stem=verb[:-2]
    ending=verb[-2:]

    conjugations=endings[ending]

except KeyError:
    print("El verbo debe terminar en ar, er o ir")
    sys.exit(1)

for index, pronoun in enumerate(pronouns):
    termination = conjugations[index]
    print(f"{pronoun} {stem}{termination}")
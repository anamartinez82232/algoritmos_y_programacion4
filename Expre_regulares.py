import re

#match = buscar al inicio
#search = buscar en cualquier parte
#findall = todas las coincidencias
# . = para encontrar cualquier caracte
# ^ = desde ahí empiza lo que buscamos
# $ = hasta ahí termina lo que buscamos
#Cuantificadores
# ? = lo que hay antes tiene que estar cero veces o una vez
# * = lo que esté antes del asterisco puede ser 0 o n veces
# + = lo que esté antes del mas puede estar 1 vez o n veces}
# {2,3} = el caracter anterior de 2 a 3 veces, "a[db]{2,3}c" que b o d se repitan 2 o 3 veces
# [a-zA-Z] = letras minusculas y mayusculas
# \d = digitos
# \w = todas las letras, numeros y signos
# \s = espacios

"""
EJEMPLO 1
EIO 805
"^[A-Z]{3}\s?\d{3}$" para la placa de un carro

EJEMPLO 2
texto = "El precio es $100.00 (cien dolares)"
resultado = re.search(r"\$100\.00", texto) para encontrar el numero
print(bool(resultado))
resultado = re.search(r"^\(.+\)", texto) para encontrar lo que hay en el parentesis

EJERCICIO 3
Para un celular
texto = ""
resultado = re.search(r"^(3\d{2})[-\s]?([\d]{3})[-\s]?([\d]{2})[-\s]?([\d]{2})$)", texto)'

EJERCICIO 4 
CORREO
"^([A-Za-z0-9\_\-\.])+@([A-Za-z\d])+\.[A-Za-z]{3})+\.([A-Za-z])+(\.[A-Za-z])?$"
"""
#EJERCICIO 4
#FECHA

def validar_fecha(fecha):

    correcta = re.search(r"^(0[1-9]|[12]\d|3[0-1])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}$", fecha)
    return bool(correcta)

print(validar_fecha("12-12-2099"))

#EJERCICIO 5
def validar_correo(correo):
    "^([A-Za-z0-9\_\-\.])+@([A-Za-z\d])+\.[A-Za-z]{3})+\.([A-Za-z])+(\.[A-Za-z])?$"

def validar_contrasena(contrasena):
    if len(contrasena) < 8
        return False
    elif bool(re.search(r"[A-Z]", contrasena))
        return False
    elif bool(re.search(r"[a-z]", contrasena))
        return False
    elif bool(re.search(r"[0-9]", contrasena))
        return False
    elif bool(re.search(r"[*¡!+%]", contrasena))
        return False
    return True



personas = []
while True:
    print("Seleccionar opción")
    print("1. Registrar persona")
    print("2. Salir")

opcion = int(input())
if opcion == 1:
    correo = input("Ingrese el correo")
    if validar_correo(correo):
        contrasena = input("Ingrese la contraseña")
        if validar_contrasena(contrasena):
            personas.append((correo, contrasena))
            {}


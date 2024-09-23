 # if si la condición se cumple se ejecuta
 # elif si no se cumple fijate en el otro
 # else si no se ejecuta la otra
 # se utiliza if condicion :

if 10 > 91:
    print('Es correcto')

else:
    print('No es correcto')
print('*'  * 30)

mascota = 'pez'

if mascota == 'gato':
     print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perrro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé qué animal tinee')

print('*' * 30)

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')

# Ejercicio 1
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

# f"{num1} es mayor que {num2}"
# "num2 es mayor que num1"
# "num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#Ejercicio 3
edad = 16
tiene_licencia = False


if (edad > 18) and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

# Ejercicio 3
habla_ingles = True
sabe_python = False

if (habla_ingles == False) and (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif (habla_ingles == False):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Cumples con los requisitos para postularte")
from sys import flags

nombre = input("¿Cúal es su nombre?: ")
ventas = int(input("¿Cuánto vendiste en el mes?: "))
total = round((ventas * 13) / 100, 2)
print(f"Hola, {nombre} tus comisinoes de este mes son de ${total}")



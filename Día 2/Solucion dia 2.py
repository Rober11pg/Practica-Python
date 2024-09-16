# solución del profe
nombre = input("Porfavor, dime tu nombre: ")
ventas = input("Digas sus ventas totales del mes: ")

ventas = int(ventas)

comision = ventas * 13 / 100

comision = round(comision, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
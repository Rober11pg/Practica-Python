"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
# Operadores Arimeticos
print(1 + 2)
print(2 - 1)
print(3 * 1)
print(4 / 2)

# Operadores lógicos AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Operadores lógicos OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Operadores lógicos NOT
print(not True)
print(not False)


# Operedaores de comparación > < >= <= != ==

v1 = 2
v2 = 2.0
print("v1 == v2: ", v1 == v2)
print(type(v1 == v2))
print("v1 != v2: ",v1 != v2)
print("v1 > v2: ",v1 > v2)
print("v1 < v2: ", v1 < v2)
print("v1 >= v2: ", v1 >= v2)
print("v1 <= v2: ", v1 <= v2)

# asignación =
print("Asignación =")
x = 2
print(x)
x = 5
print(x)

# asignación +=
print("Asignación +=")
x = 5
x += 1
print(x)

# asignación operador -=
print("Asignación -=")
x = 5
x -= 1
print(x)


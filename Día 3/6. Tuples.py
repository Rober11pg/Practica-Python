# Los tuples son inmutables, no se puede reasignar
# ocupan menos espacio de memoria, aprueba de daños
# son apruebas de daños
# se debe asignar el mismo número de variables que tiene el tuple

mi_tuple = (1,2,(10, 20) ,4)
t = (5, 'hola', 5.6)

print(type(mi_tuple))
print(mi_tuple[2][0])


# se puede hacer casting, cambiar a otra conversión
mi_tuple = list(mi_tuple)

print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

# asignar el contenido de un tuple a diferentes variables
t = (1, 2, 3, 1)

# se asigna la misma cantidad de valores que de variables
# se puede hacer con las listas y diccionarios
x,y,z, a = t
print(x, y, z, a)

print(len(t))

# cantidad de veces que se repite el valor que está dentro del tuple
print(t.count(1))

# consulta el número de indice que se ecuentra el valor
print(t.index(2))


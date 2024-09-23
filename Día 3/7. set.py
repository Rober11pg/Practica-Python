# se puede utiliar set () o directamente {}
# si son de un solo argumento entonces se utiliza ([]) las llaves o paretesis
# NO TIENE ORDEN COMO LAS LISTAS
# Solo admiten elementos únicos, no están ordenados en índices
# no se puede incluir lista y diccionarios

# quiere un solo argumento por eso utiliza []
mi_set = set([1,2,3,4,5,1,(1,2,3),3,1]) # los tupple son inmultables por eso deja ingresar, las repeticiones se borran
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)


# NO se puede hacer esto -> print(mi_set[0])

print(len(mi_set))

# Sirve para ver si se ecuentra el número en el set
print(2 in mi_set)


s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print("s3: ", s3)

# Sirve para agregar valores
s1.add(4)
s1.add(2)
print(f"add sirve para agregar valroes: {s1}")

# Sirve para borrar
s1.remove(2)
print(f"remove sirve para remover o eliminar valroes: {s1}")

#Es igual que remover solo que si no existe el elemento que vas a elminar no te da error como remover
s1.discard(5)
print(f"discard sirve para qutiar valores: {s1}")

# Elimina un elemento aleatorio
sorteo = s1.pop()
print(f"pop sirve para remover un elemento aleatorialmente: {sorteo}")

# Vaciar al set
s1.clear()
print(f"clear vacia el set: {s1}")


# Practica
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
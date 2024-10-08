# Secuencias ordenadas de objetos
# Puedes estar compuestas por diferentes objetos
# Listas de listas
# Los string son una lista de caracteres
# Las listas son mutables los string no


# Las listas en python puede contener diferentes tipos de datos
mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
otra_lista = ["hola", 55, 6.10]

# Sirve para devolver el tamaño de la lista
resultado = len(mi_lista)

# indice
resultado = mi_lista[0:]
print(type(mi_lista))
print(resultado)

print("Lista unida")
mi_lista3 = mi_lista + mi_lista
print(mi_lista3)

# Los string no puedea alterar sus elementos pero la lista si puede
mi_lista3[0] = "alfa"

# appen agregar
mi_lista3.append("g")
print(mi_lista3)

# Pop sin parametros, elimina el último elemento
mi_lista3.pop()

# esto con índice
mi_lista3.pop(2)
print(mi_lista3)

eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

# ordenar listas de forma ascendente
print("Sort no devuelve nada solo ordenada, indica un objeto que no tiene valor")
lista = ['g', 'o', 'b', 'm', 'c']
lista_original = lista
print(lista)

# reordena la lista
lista.sort()

print(lista)

print("#" * 40)


# Ordena de forma descendente
print(lista)
lista.reverse()
print(lista)
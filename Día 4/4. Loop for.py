# Loops son bucles
# Iterar n veces para que se cumpla la condición
# iterable repasar sus elementos internos se puede hacer eso con las listas

# Se repiten cantidad definidad y indefinida

lista = ['a', 'b', 'c', 'd']
for i in lista:
    num_letra = lista.index(i) + 1 # numero de intereaciones
    print(f"Letra {num_letra}: {i}")

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'): # startswith chequea si comienza con un determinado caaracter
        print(nombre)
    else:
        print("Nombre que o mienza con L")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)


palabra = 'python es genial'
for letra in palabra:
    print(letra)

for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2':'b', 'clave3':'c'}
for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a, b in dic.items():
    print(a, b)
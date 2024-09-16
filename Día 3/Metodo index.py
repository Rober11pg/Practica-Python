mi_texto = "Esta es una prueba"
# Python cuenta de derecha a izquierda
# index busca de derecha a izquierda

#resultado = mi_texto.index("a", 5, 10)

# Busca de derecha a izquierda
resultado = mi_texto.rindex("a")

print(resultado)


palabra = "ordenador"

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))


frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))

print("frase 2")
frase2 = "Hola mundo"
print(frase2.find("world"))
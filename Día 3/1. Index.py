mi_texto = "Esta es una prueba"
# resultado = mi_texto[-4]

# donde comienza el substring, es sensible a las mayusculas
resultado1 = mi_texto.index("s", 5,10)

# rindex buscar de derecha a izquierda
resultado2 = mi_texto.index("e", 2,10)

print(resultado1)
print(resultado2)

# comparar entre dos o mas cosas and, or, not
mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)

mi_bool = 10 == 10 or 3 == 3
print(mi_bool)


texto = "esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

#
mi_bool = not ('a' == 'a')
print(mi_bool)

# Ejercicio 1
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 >num2) and (num1 < num3)

# Ejercicio 2
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 >num2) or (num1 < num3)

# Ejercicio 3
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not palabra1 in frase or palabra2 in frase
print(mi_bool)
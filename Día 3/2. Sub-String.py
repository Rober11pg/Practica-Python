# Slicing rebanar o cortar en rebajas
texto = "ABCDEFGHIJKLM"
# : 5 sirve para interpretar hasta que finalice
fragmento = texto[2:5:3] # se va a saltar de 3 en 3
print(fragmento)

fragmento = texto[::3] # se va a saltar de 3 en 3
print(fragmento)

fragmento = texto[::-1] # Escribe en orden inverso
print(fragmento)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])



# Cuantas veces aparece cada letra lista, contar cuantas veces
# Cuantas palabras hay en total transformar en una lista
# Primera y úlitma letra
# Palabras en orden inverso
# aparece la palabra python


parrafo = input("Ingrese un texto que le guste: ")

print("Ingrese 3 letras a su elección que desea ver cuantas veces se repite")
letra1 = input("Primera letra: \n")
letra2 = input("Segunda letra: \n")
letra3 = input("Tercera letra: \n")

parrafo = parrafo.lower()


# 1. Contar cúantas veces aprece cada una de las letras que eligio
print("1. Cantidad de veces que se repiten")
print(f"Primera letra es la '{letra1}' se cuenta {parrafo.count(letra1)} veces ")
print(f"Segunda letra es la '{letra2}' se cuenta {parrafo.count(letra2)} veces ")
print(f"Tercera letra es la '{letra3}' se cuenta {parrafo.count(letra3)} veces \n")

palabras = parrafo.split()
lista = palabras

# 2. Cuantas palabras hay a lo largo de toda el texto
print(f"2. El largo de una lista es: {len(lista)}\n")

# 3. Tercero cual es la primera letra del texto y la última
print(f" 3. La primera letra de texto es: {parrafo[0]}")
print(f" La última letra de texto es: {parrafo[-1]}\n")

# 4. Texto invertido (orden de las palabras)
lista.reverse()
texto_invertido = " ".join(lista)
print(f"4. El texto invertido: {texto_invertido}\n")

# 5 Verficar si la palabra 'Python' está en el texto
if "python" in parrafo:
    print("5. La palabra 'python' se encuentra en el texto.")
else:
    print("5. La palabra 'python' no se encuentra en el texto.")
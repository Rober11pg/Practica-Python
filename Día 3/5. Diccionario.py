# Los diccionarios no tinen un orden específico
# Diccionarios no importa el orden
# Clave valor, cuando quieres consultar cosas específicas
# por ejemplo las caracterísitcas de una persona
# Los diccionario puede contener listas y diccionarios a su vez 

diccionario = {'c1' : 'valor1', 'c2' : 'valor2'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)

# Diccionario puede contener lista o diccionarios
cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.75}
consulta = (cliente['talla'])
print(consulta)
print("#" * 20)
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

# Ejercicios práctico
print("#" * 20)
dic2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}

# Imprima la letra e pero en mayuscula
print(dic2['c2'][1].upper())

# Como hacer para agregar elementos que ya haya sido creado
dic3 = {1:'a', 2:'b'}
print(f"{dic3}")

# Crea una nueva clave con su valor
dic3[3] = 'c'
print(f"sirve paraa agregar una nueva valor al diccionario {dic3}")

# sobreescribir
dic3[2] = 'B'
print(dic3)


# conocer todas las claves que hay
print(f"Sirve para conocer todas las claves que hay en las claves {dic.keys()}")

# conocer solo los valores
print(f"Sirve para conocer los valores del diccionario {dic.values()}")

# conocer todo
print(f"Sirve para conocer todo {dic.items()}")

print('#' * 30)
print("Practica")
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])
mi_dict['puntos']['points2'][1] = 11
print(mi_dict['puntos']['points2'][1])



# Practica
dicGoku = {"nombre": "Goku", "edad": 52, "pacatiempo": "pelear", "familia": {"mujer": "Bulma", "hijo": "Gohan", 'maestro': "roshi", 'numeros': ['uno', 'dos', 1, 2]}}
# Quien fue el maestro de goku
print(f"El maestro de Goku fue: {dicGoku['familia']['numeros'][0]}")
# Booleno se lo pruede declarar demanera directa o indirecta
# Permite comparacion indirecta con los operadores lógicos
# Los boleanos son importantes para la inteligencia artificial

var1 = True
var2 = False
print(type(var1))
print(var1)

# Manera indirecta
numero1 = 5 ==2 + 3
numero2 = 5 > 2 + 3
print(type(numero1))
print(f"Numero 1 {numero1}")
print(type(numero2))
print(f"Numero 2 {numero2}")




numero = 5 >= 2 + 3
print(type(numero))
print(numero)

numero = bool(5 > 6 )
print(type(numero))
print(numero)

# in también podría servir como un control para los booleanos
lista = [1,2,3,4]
control = 5 not in lista
print(type(control))
print(control)

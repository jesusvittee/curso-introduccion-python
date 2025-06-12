#not
print('NOT')
print(not True)  # False
print(not False)  # True
print(not (True and False))  # True
print(not (True or False))  # False
# Comparaciones
print('Comparaciones')
print(10 == 10)  # True
print(10 != 10)  # False
print(10 > 5)  # True
print(10 < 5)  # False
print(10 >= 10)  # True
print(10 <= 10)  # True
# Combinando operadores lógicos
print('Combinando operadores lógicos')
print(True and (False or True))  # True
print((10 > 5) and (10 < 15))  # True
print((10 > 5) or (10 < 5))  # True
print((10 > 5) and (10 < 5))  # False

# Operadores de identidad
print('Operadores de identidad')
print('a' is 'a')  # True, porque ambos apuntan al mismo objeto en memoria
print('a' is not 'b')  # True, porque son objetos diferentes
print([1, 2, 3] is [1, 2, 3])  # False, porque son listas diferentes en memoria
print([1, 2, 3] is not [1, 2, 3])  # True, porque son listas diferentes en memoria
# Operadores de pertenencia
print('Operadores de pertenencia')
print('a' in 'abc')  # True, porque 'a' está en la cadena 'abc'

print('d' in 'abc')  # False, porque 'd' no está en la cadena 'abc'
print(1 in [1, 2, 3])  # True, porque 1 está en la lista [1, 2, 3]
print(4 in [1, 2, 3])  # False, porque 4 no está en la lista [1, 2, 3]

print('a' not in 'abc')  # False, porque 'a' está en la cadena 'abc'

stock = input('ingrese cantidad: ')
Valor_Stock = int(stock)

Revision_Stock = (not(Valor_Stock >= 100 and Valor_Stock <= 1000))
print(Revision_Stock)

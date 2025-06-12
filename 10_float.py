x = 3.3
print(x)

y= 1.1 + 2.2
print(y)

print(x == y)  # Esto puede dar False debido a la precisión de los flotantes

y_str = format(y, '.2g')
print(y_str)
print('str ', y_str)
print(y_str == str(x))  # Esto debería ser True
print('x' * 30)

print(y,x) # Sirve para comparar valores
tolerance = 0.0000000000000001
print(x-y)
print(abs(x - y) < tolerance)  # Compara si la diferencia es menor que la tolerancia
""""
aprendí que abs() es para obtener valores absolutos -5 a abs 5
"""
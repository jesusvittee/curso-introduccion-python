nombre = 'Jesus'
apellido = 'Nicolás Vite'

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)
quote = 'I´m Jesus'
print(quote)

quote2 = 'He said "Hello"'
print(quote2)

#format
template = 'Hello, my name is ' + nombre + ' and my last name is ' + apellido
print('v1', template)

"""
Basicamente en este apartado puedo escribir un texto en donde agrego unos corchetes que tras un punt format puedo agregar los valores que quiero que se muestren en esos corchetes.
"""
#format con .format
template2 = 'Hello, my name is {} and my last name is {}'.format(nombre, apellido)
print('v2', template2)



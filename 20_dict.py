person = {
    'name':'Jesus',
    'last_name':'nicolas',
    'langs': ['python', 'javascript'],
    'age': 21
}

print(person)
person['name'] = 'Seúl'
person['age'] -= 2

person['langs'].append('rubi')

print(person)

#eliminar atributo con del
del person['last_name']

person.pop('age') # se deben de enviar las llaves para eliminar
#dentro de pop requier un argumento obligatoriamente

print(person.items()) #obtener los items del diccionario, me los da en forma de tupla
print(person.keys()) #devuelve una lista de las llaves
print(person.values())# me devuelve los valores en forma de lista

#update
person.update({'escuela':'TecNM'})
print(person)

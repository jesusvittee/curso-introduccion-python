my_dict = {}

print(type(my_dict))


my_dict = {
'nombre' : 'jesus',
'apellido' : 'nicolas',
'edad' : 23
} #key : value

#leer cuanto objetos tenemos en el diccionario

print(my_dict)
print(len(my_dict))

#obtener valor
print(my_dict['nombre'])
#segunda manera
print(my_dict.get('comida', 'No proporcionado'))

#preguntar si esta un objeto
print('avion' in my_dict) #Preguntas por la llave

my_dict['nombre'] = 'Jhon'

print(my_dict)
"""
for element in range(20):
    print(element)

#comenzar del rango 1
for element in range(1,20):
    print(element)

"""
"""
#iteracion de lista
my_list  = [23, 45, 67, 89,43]

for element in my_list:
    print(element)
"""
"""
#iteracion de tuple
my_tuple = ('Jesus','Nicolas', 'vite')
for element in my_tuple:
    print(element)
"""
#obtener valores y llaves
product = {
    'nombre' : 'Burgerking',
    'producto' : 'Amburgesa',
    'precio' : 240
}    
for key in product:
    print(key)
    print(product[key])
    print(key, product[key]) 
    
#o de esta manera
for key, value in product.items():
    print(key, value)
    
    
people = [
    {'name':'jesus',
     'age' : 21
    },
     {'name':'Alexander',
     'age' : 24
     }
]
#obtengo los diccionarios
for person in people:
    print(person)
    print('-'*20)
    print(person['name'])
    
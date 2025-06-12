#CRUD create, read, update and delete
numbers = [1,2,3,4,5,6]
print(numbers[2])

numbers[-1] = 29
print(numbers)

#agregar
numbers.append(49) #agregar un nuevo elemento, agregado al final de la lista
print(numbers)

numbers.insert(3,'Inseté un valor en el 3') #Crear un espacion no se borra
print(numbers)

task = ['Todo 1', 'Todo2']

#union de lista
fusion_list = numbers + task
print(fusion_list)

#preguntar por la posicion de un elemento
index = fusion_list.index('Todo 1')
print(index)

#fusion_list(index) = 'Change todo 1'
#print(fusion_list)

#Eliminar
fusion_list.remove('Todo2')

print(fusion_list)

fusion_list.pop()
print(fusion_list)

fusion_list.pop(0)
print(fusion_list)

fusion_list.reverse()
print(fusion_list)

#ordenar numeros
numbers_a = [1,2,4,5,3]
numbers_a.sort()
print(numbers_a)

strings = ['pan', 'jamón', 'tosino']
strings.sort()
print(strings)


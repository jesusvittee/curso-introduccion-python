values = [3,4,6,7,9,10,1,2,5,6]

print(values[4])

values[4] = 'Nueve'

#Slicing
#La manera en como accedo a estos valores para los cambios de datos tipo estring
values[4] = values[4].upper()
values[4] = values[4].lower()
values[4] = values[4].swapcase()
values[4] = values[4].capitalize()
values[4] = values[4].startswith('N')
values[4] = values[4].endswith('e')

print(values[4])
print(values[1:6:2])

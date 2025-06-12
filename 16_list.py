numbers = [1,2,3,8,5,6,7]
print(numbers)
print(type(numbers))

tasks= ['Make cook', 'Make a drawing']
print(tasks)
print(type(tasks))

types = [4, False, 'Yes']
print(types)

print(numbers[3]) # number[3] = 8 
print(tasks[1])

#Mutaciones: actulizar elementos en particular
tasks[1] = 8
print(tasks)

print('Slicing', numbers[3:4])
print(False in types)
print('Yes' in types)

text = "Ella es una buena cantante"

print('Python' in text)
print('Ella' in text)

if 'cantante' in text:
    print("Que bien")
else:
    print("No hay manera de que ella no sea cantante")
    
size = len('Glorioso amor')
print(size)

#Metodos de strings
print(text, text.upper()) #pasar valores a mayusculas
print(text, text.lower()) #pasar valores a minusculas

print(text, text.count('e')) #saber cuantas reps, hay en el texto

print(text.swapcase()) #convierte primer valor en minuscula

print(text.startswith("Ella")) #Pregunta si el text comienza con tal palbra

print(text.replace('Ella', 'El')) #cambia las palabras del texto

text2 = 'La comidad de mi mamá es exquisita'
print(text2)
print(text2.capitalize()) 
print(text.title())
print(text2.isdigit())
print('84848'.isdigit())

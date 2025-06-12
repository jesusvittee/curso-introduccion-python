"""
Justo comenzaré a redactar sobre como manipular los números en Python.
"""
#Partido de Free Fire"
Vida = 300
print("Vida del personaje: ", Vida)
#datos tipo Float
hp = 299.3
print("Este contador no sirve: {}".format(hp))

print(type(Vida))
print(type(hp))

#Es posible manipular los datos con sus mismos datos tal como
Vida = Vida + Vida
#o
hp = hp + hp
print("Vida: {}, HP {} ".format(Vida, hp))

#Por ultimo los datos pueden reducirse o aumentar

Vida -= Vida + 2
print(Vida)
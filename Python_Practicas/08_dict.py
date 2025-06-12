Mascotas = {
    'raza':'Husky',
    'nombre':'Poli',
    'edad':3,
    'color':'Blanco',
}
raza = Mascotas['raza']
nombre = Mascotas['nombre']
edad = Mascotas.get('edad')
color = Mascotas.get('color')
genero = Mascotas.get('genero','No especificado')

print(f'Verifique que los datos de su mascota son correctos: \n {raza}, {nombre}, {edad}, {color}, {genero}.')

cambiar = input('¿Gusta realizar un cambio? yes or not: ')
if cambiar == 'yes':
   cambio = input('''Ingresa lo que quieras cambiar: 
          1. raza
          2. nombre
          3. edad
          4. color
          5. genero
          ''')
   cambio = int(cambio)
   if cambio == 1:
    cambiar_raza = input('Raza del perro: ')
    Mascotas['raza'] = cambiar_raza
    print(Mascotas)
   elif cambio == 2:
    cambiar_nombre = input('nombre del perro: ')
    Mascotas['nombre'] = cambiar_nombre
    print(Mascotas)
   elif cambio == 3:
    cambiar_edad = input('edad del perro: ')
    Mascotas['edad'] = cambiar_edad
    print(Mascotas)
   elif cambio == 4:
    cambiar_color = input('color del perro: ')
    Mascotas['color'] = cambiar_color
    print(Mascotas)
   elif cambio == 5:
    cambiar_genero = input('genero del perro: ')
    Mascotas['genero'] = cambiar_genero
    print(Mascotas)
else:
    print('que tengas un buen día')
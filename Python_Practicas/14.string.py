frace = input('Ingresa una frace o texto: ')
Mostrar = frace
print('Procesando...')
"""
print('Texto a Mayusculas: ', frace.upper())
print('Texto a Minuscula: ', frace.lower())
print('Texto invertido: ', frace.swapcase())
print('Primera palabra en mayuscula: ', frace.capitalize())
print('Longitud de texto: ', len(frace))

rep = 'Que vocal quieres saber cuanto se repite?'

print('Pabra que se repite muchas veces: ', frace.count(rep))
print('El texto es un digito?: ', frace.isdigit())

comienza = input('El texto inicia con?')
termina = input('El texto termina con?')
print('Texto comienza con: ', frace.startswith(comienza))
print('Texto termina con: ', frace.endswith(termina))
"""
palabra = 'Palabra a remplazar de "{}": '.format(Mostrar)
palabras = input(palabra)
remplazar = f'Agrega palabra nueva para cambiar a "{palabras}": '
rem= input(remplazar)
print('Remplazo texto: ', frace.replace(palabras, rem))
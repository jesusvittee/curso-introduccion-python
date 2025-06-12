#Concatenacion String

#Menú
libros = 'libros que he leido: '
libro1 = '7 habitos de la gente altamente efectiva'
libro2 = 'Hábitos atomicos'
libro3 = 'Las 4 horas laborales'
libro4 = 'The holy man'

leidos = 'Formatos 1:{} {}, {}, {}, {}.' .format(libros,libro1,libro2, libro3, libro4)
leidos2 = f'Formatos 2: {libros} {libro1}, {libro2}, {libro2}, {libro3}, {libro4}'
leidos3 = 'Formato 3: ' + libros + ' ' + libro1 + ', ' + libro2 + ', ' + libro3 + ', ' + libro4 + ', '
print(leidos)
print(leidos2)
print(leidos3)

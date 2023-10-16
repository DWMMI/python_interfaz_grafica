#! -> Esto se llama shebang o hashbang, en la primera línea para indicar la ruta del intérprete

# ! /usr/bin/env python <- Este es solamente un ejemplo.
edad = 23
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# Cada bloque de instrucciones dentro de una estructura de control debe estar tabulada.
num = 0
if num >= 0:
    while num < 10:
        print(num)
        num += 1

# El punto y coma se puede usar para separar varias sentencias en una misnma linea, pero no se aconseja su uso.
edad = 15;
print(edad)

# Cuando el bloque a sangrar sólo ocupa una línea ésta puede escribirse después de los dos puntos.
color = 'azul'
if color == 'azul': print('cielo')

# La barra invertida \ permite escribir una línea de código demasiado extensa en varias líneas
'''
if condicion1 and condicion2 and condicion3 and \
    condicion4 and condicion5:
'''

# Las expresiones entre parentesis, llaves o corchetes pueden ocupar varias líneas
dias = ['Lunes', 'Martes', 'Miercoles',
        'jueves', 'viernes']

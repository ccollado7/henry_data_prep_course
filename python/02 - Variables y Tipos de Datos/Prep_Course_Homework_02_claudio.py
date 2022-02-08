## Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

var_1 = 10
print(var_1)

#2) Imprimir el tipo de dato de la constante 8.5

var_2 = 8.5
print(type(var_2))

#3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(var_2))

#4) Crear una variable que contenga tu nombre

var_4 = 'Claudio'

#5) Crear una variable que contenga un número complejo

var_5 = 1 + 1j

#6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(var_5))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

import numpy as np
var_7 = np.pi
print(round(var_7,4))

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var_8a = 'True'
var_8b = True

print(var_8a == var_8b)

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print(type(var_8a))
print(type(var_8b))

#10) Asignar a una variable, la suma de un número entero y otro decimal

var_10a = 10
var_10b = 2.3
var_10 = var_10a + var_10b
print(var_10)

#11) Realizar una operación de suma de números complejos

var_11a = 1 + 1j
var_11b = 2 + 2j
var_11 = var_11a + var_11b
print(var_11)

#12) Realizar una operación de suma de un número real y otro complejo

var_12a = 7
var_12b = 2 + 2j
var_12 = var_12a + var_12b
print(var_12)

#13) Realizar una operación de multiplicación

var_13 = 2 * 10
print(var_13)

#14) Mostrar el resultado de elevar 2 a la octava potencia

var_14 = 2**8
print(var_14)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

var_15 = 27 / 4
print(var_15)

#16) De la división anterior solamente mostrar la parte entera

var_16 = 27 // 4
print(var_16)

#17) De la división de 27 entre 4 mostrar solamente el resto

var_17 = 27 % 4
print(var_17)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

var_18 = (4 * var_16 ) + var_17
print(var_18) 

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

var_19 = 'Gato ' + 'Perro'
print(var_19)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print('2' == 2)

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(int('2') == 2)
print('2' == str(2))

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

a = float('3.8') #La definicion de un numero flotante corresponde al uso del punto .
print(a)

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var_23 = 3
var_23 -= 1
print(var_23)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(1 << 2)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print(2 + 2) #resultado 4
print('2' + '2') #resultado '22' ya que realiza la concatenacion

#26) Realizar una operación válida entre valores de tipo entero y string

var_26 = 2 * '2' #operacion valida
print(var_26)
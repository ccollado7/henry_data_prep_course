#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

var_1 = 10
if var_1 < 0:
    print(f'{var_1} es menor que 0')
elif var_1 > 0:
    print(f'{var_1} es mayor que 0')
else:
    print(str(var_1) + ' es igual a 0')


#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

var_2a = True
var_2b = 10

if type(var_2a) == type(var_2b):
    print(f'{var_2a} es del mismo tipo que {var_2b}')
else:
    print(f'{var_2a} no es del mismo tipo que {var_2b}')

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for i in range(1,21):
    if i%2 == 0:
        print(f'{i} es un numero par')
    else:
        print(f'{i} es un numero impar')

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0,6):
    pot = i**3
    print(f'la potencia 3 de {i} es {pot}')

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

var_5 = 10
for i in range(1,var_5+1):
    print(i)

#6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

var_6 = 10
factor = 1
if var_6 <= 0:
    print(f'el numero {var_6} ingresado no es un numero valido')
elif var_6 == 0 or var_6 == 1:
    print(f'el factor de {var_6} es {factor}') 
else:
    while var_6 > 1:
        factor = factor * var_6
        var_6 = var_6 - 1
    print(f'el factor del numero ingresado es {factor}')

#7) Crear un ciclo for dentro de un ciclo while

n = 5
m = 3
while n > 0:
    print(f'Ciclo while Nº {n}')
    for i in range(1,m):
        print(f'Ciclo for Nº {i}')
    n = n - 1
    m = m + 1

#8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(n):
    print(f'Ciclo for Nº {i}')
    m = 3
    while m > 0:
        print(f'Ciclo while Nº {m}')
        m = m - 1

#9) Imprimir los números primos existentes entre 0 y 30

a = 0
b = 30
for i in range(a,b+1):
    contador_primo = 0
    if i == 0 or i == 1:
        pass
    elif i > 1:
        for j in range(1,i+1):
            if i%j == 0:
                contador_primo = contador_primo + 1
        if contador_primo == 2:
            print(f'{i} es numero primo')

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin


#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

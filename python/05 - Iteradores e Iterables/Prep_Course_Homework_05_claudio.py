## Iteradores e iterables

#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

list_1 = []
num = -15
while num<0:
    list_1.append(num)
    num = num + 1
print(list_1)

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

lista_2 = list(range(-15,0))
num = 0
while num < len(lista_2):
    if lista_2[num]%2 == 0:
        print(f'{lista_2[num]} es un numero par')
    num = num + 1

#3) Resolver el punto anterior sin utilizar un ciclo while

lista_3 = list(range(-15,0))
for num in lista_3:
    if num%2==0:
        print(f'{num} es un numero par')

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

lista_3 = list(range(-15,0))
for i in lista_3[0:3]:
    print(i)

#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

lista_3 = list(range(-15,0))
for i,v in enumerate(lista_3):
    print(f'En el indice {i} se encuentra el elemento {v}')

#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista = [1,2,5,7,8,10,13,14,15,17,20]
for i,v in enumerate(lista):
    if i == 0 :
        pass
    elif v == lista[-1]:
        break
    else:
        if lista[i+1] == v + 1:
            pass
        else:
            lista.insert(i+1,v+1)
print(lista)

#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula.... Crear una lista con los primeros treinta números de la sucesión

n1 = 0
n2 = 30
fibo = []
for n in range(n1,n2):
    if (n == 0) or (n == 1):
        fibo.append(n)
    else:
        sum = fibo[-2] + fibo[-1]
        fibo.append(sum)
print(fibo)

#8) Realizar la suma de todos elementos de la lista del punto anterior

suma = 0
for k in fibo:
    suma = suma + k
print(suma)

#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. 
# Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos: Donde i es la cantidad total de elementos

number = 5
num_aureo =[]
for i in range(-number-1,-1):
    div = fibo[i+1] / fibo[i]
    num_aureo.append(div)
print(num_aureo)

#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n" cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
letra = 'n'
count = 0
for i in cadena:
    if i == letra:
        count = count + 1
    else:
        pass
print(f'La letra {letra} apare {count} veces en la cadena')

#11) Crear un diccionario e imprimir sus claves utilizando un iterador

d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}

for clave in d1.keys():
    print(clave)

#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
lista_cadena = [i for i in cadena if i!=' ' if i!='.']
for letra in lista_cadena:
    print(letra)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

list1 = [i for i in range(5)]
list2 = ['Claudio','Guille','Rafa','Casa','Auto']
union = zip(list1,list2)
print(type(union))
print(list(union))

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7 lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
div = 7
list_7 = []
for num in lis:
    if num%7 == 0:
        list_7.append(num)
print(list_7)

#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
count = 0
for i in lis:
    if type(i) is not list:
        count = count + 1
    else:
        for k in i:
            count = count + 1
print(count)

#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i,v in enumerate(lis):
    if type(v) is not list:
        new_list = [v]
        lis[i] = new_list
    else:
        pass
print(lis)
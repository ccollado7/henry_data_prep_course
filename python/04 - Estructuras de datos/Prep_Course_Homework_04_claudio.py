## Estructuras de Datos

#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

lista_1 = ['Buenos Aires', 'San Pablo','Caracas','Santiago de Chile','Lima','Distrito Federal']
for i in lista_1:
    print(i)

#2) Imprimir por pantalla el segundo elemento de la lista

print(lista_1[1])

#3) Imprimir por pantalla del segundo al cuarto elemento

print(lista_1[1:4])

#4) Visualizar el tipo de dato de la lista

print(type(lista_1))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(lista_1[2:])

#6) Visualizar los primeros 4 elementos de la lista

print(lista_1[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

lista_1.append('Buenos Aires') #incluir elementos repetidos no genera error
lista_1.append('Madrid')
print(lista_1)

#8) Agregar otra ciudad, pero en la cuarta posición

lista_1.insert(3,'Barcelona')
print(lista_1)

#9) Concatenar otra lista a la ya creada

lista_2 = ['Berlin','Moscu','New York']
lista_1.extend(lista_2)
print(lista_1)

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(lista_1.index('Buenos Aires')) #de esta forma se retorna el indice del primer elemento que encuentra. No retorna el indice de la ciudad repetida agregada

indices_bs = [i for i, x in enumerate(lista_1) if x == "Buenos Aires"] #Utilizando list comprehension se encuentran todos los indices
print(indices_bs)

#11) ¿Qué pasa si se busca un elemento que no existe?

    #lista_1.index('Calcuta') si el elemento no se encuentra en la lista se obtiene un error 'ValueError'

#12) Eliminar un elemento de la lista

lista_1.remove('Berlin')
print(lista_1)

#13) ¿Qué pasa si el elemento a eliminar no existe?

    # lista_1.remove('Sidney') si el elemento a eliminar no existe entonces se obtiene un error 'ValueError'

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

last_element = lista_1.pop()
print(last_element)

#15) Mostrar la lista multiplicada por 4

print(lista_1 * 4)

#16) Crear una tupla que contenga los números enteros del 1 al 20

tupla = tuple(range(1,21))
print(tupla)
print(type(tupla))

#17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[10:16])

#18) Evaluar si los números 20 y 30 están dentro de la tupla

a = 20
b = 30
print(a in tupla)
print(b in tupla)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

ciudad = 'Paris'
if ciudad not in lista_1:
    lista_1.append(ciudad)
    print(lista_1)

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

print(lista_1.count('Buenos Aires'))
print(tupla.count(5))   

#21) Convertir la tupla en una lista

lista_2 = list(tupla)
print(type(lista_2))

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

num1,num2,num3 = tupla[0:3]
print(num1)
print(num2)
print(num3)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

mi_diccionario = {'Ciudades' : lista_1,
                  'Pais' :['Argentina','Brasil','Venezuela','España','Chile','Peru','Mexico','Argentina','España','Rusia','Francia'],
                  'Continente' :['America','America','America','Europa','America','America','America','America','Europa','Asia','Europa']
}

print(mi_diccionario)
print(type(mi_diccionario))

#24) Imprimir las claves del diccionario

print(mi_diccionario.keys())

#25) Imprimir las ciudades a través de su clave

print(mi_diccionario['Ciudades'])

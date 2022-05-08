# Biblioteca de Python comúnmente usada en la ciencias de datos y aprendizaje automático (Machine Learning). Proporciona una estructura de datos de matriz que tiene diversos beneficios sobre las listas regulares.

import numpy as np

Crear arreglo unidimensional:
my_array = np.array([1, 2, 3, 4, 5])
Resultado: array([1, 2, 3, 4, 5])

Crear arreglo bidimensional:
np.array( [[‘x’, ‘y’, ‘z’], [‘a’, ‘c’, ‘e’]])
Resultado:
[[‘x’ ‘y’ ‘z’]
[‘a’ ‘c’ ‘e’]]

Mostrar el número de elementos del arreglo:
len(my_array)

Sumar todos los elementos de un arreglo unidimensional:
np.sum(my_array)

Obtener el número máximo de los elementos del arreglo unidimensional
np.max(my_array)

Crear un arreglo de una dimensión con el número 0:
np.zeros(5)
Resultado: array([0., 0., 0., 0., 0.])

Crear un arreglo de una dimensión con el número 1:
np.ones(5)
Resultado: array([1., 1., 1., 1., 1.])

Comando de Python para conocer el tipo del dato:
type(variable)

Ordenar un arreglo:
np.order(x)

Ordenar un arreglo por su llave:
np.sort(arreglo, order = ‘llave’)

Crear un arreglo de 0 a N elementos:
np.arange(n)
Ej.
np.arange(25)
Resultado:
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
17, 18, 19, 20, 21, 22, 23, 24])

Crear un arreglo de N a M elementos:
np.arange(n, m)
Ej.
np.arange(5, 30)
Resultado:
array([ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
22, 23, 24, 25, 26, 27, 28, 29])

Crear un arreglo de N a M elementos con un espacio de cada X valores:
np.arange(n, m, x)
Ej.
np.arange(5, 50, 5)
Resultado:
array([ 5, 10, 15, 20, 25, 30, 35, 40, 45])

Crear arreglo de NxM:
np.full( (n, m), x )
Ej.
np.full( (3, 5), 10)
Resultado:
array([
[10, 10, 10, 10, 10],
[10, 10, 10, 10, 10],
[10, 10, 10, 10, 10]
])

Número de elementos del arreglo:
len(my_array)

import numpy as np

np.array([10, 20, 24, 5, 15])
a = np.array([10, 0, 30, 20, 4, 31, 51, 24, 5, 15, 20, 24, 5, 15])

a[4] # => position 4

a[3:] # => desde la position 3

a[3:7] # => desde la position 3 to 7

a[1::4] # => print each 4 positions

np.zeros(5) # => create 5 elements with 0

np.ones((4, 5)) # row and col

types(ones)

types(ones[3])

np.linspace(3, 10, 5) # 5 elements between 3 and 10 (real numbers)

c = np.array([10, 0, 30, 20, 4, 31, 51, 24, 5, 15, 20, 24, 5, 15])
np.sort(c)

cc = [ ('name', 'S10', ('age', int))]
data = [('Juan', 10), ('Mary', 32), ('James', 29)]
users = np.array(data, dtype = cc)
np.sort(users, order = 'age')

np.arange(25)

np.arange(5, 50, 5) # elements from 5 to 5, inc = 5

np.full((3,5), 10) # matrx 5,3

np.diag([0,3,9,10]) # matrix diagonal

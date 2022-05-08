Pandas
Pandas es una herramienta de manipulación de datos de alto nivel, es construido con la biblioteca de Numpy. Su estructura de datos más importante y clave en la manipulación de la información es DataFrame, el cuál nos va a permitir almacenar y manejar datos tabulados observaciones (filas) y variables (columnas).

Importar la biblioteca:
import pandas as pd

Generar una serie con Pandas:
pd.Series([5, 10, 15, 20, 25])
Resultado:
0 5
1 10
2 15
3 20
4 25

Crear un Dataframe:
lst = [‘Hola’, ‘mundo’, ‘robótico’]
df = pd.DataFrame(lst)
Resultado:
0
0 Hola
1 mundo
2 robótico

Crear un Dataframe con llave y dato:
data = {‘Nombre’:[‘Juan’, ‘Ana’, ‘Toño’, ‘Arturo’],
‘Edad’:[25, 18, 23, 17],
‘Pais’: [‘MX’, ‘CO’, ‘BR’, ‘MX’] }
df = pd.DataFrame(data)
Resultado:

Resultado Data Frame.png
Leer archivo CSV:
pd.read_csv(“archivo.csv”)

Mostrar cabecera:
data.head(n)

Mostrar columna del archivo leído:
data.columna

Mostrar los últimos elementos:
data.tail()

Mostrar tamaño del archivo leído:
data.shape

Mostrar columnas:
data.columns

Describe una columna:
data[‘columna’].describe()

Ordenar datos del archivo leído:
data.sort_index(axis = 0, ascending = False)

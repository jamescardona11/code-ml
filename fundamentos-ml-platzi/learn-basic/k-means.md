- Algoritmo no supervisado.
- Crea K grupos a partir de observaciones de un set de datos.
- Trata información que no tiene etiquetas asignadas.
- Agrupa información basada en sus características.
- K = centroides
- Aproximación a K: método del codo
- Aplicaciones:
- Segmentación por comportamiento:
- por historial de compras
- actividad en una aplicación móvil, web
- Definir personas basadas en sus intereses.
- Crear perfiles basado en el monitoreo de actividad.
- Ordenando medidas de sensores:
- Detecta tipos de actividades en sensores de movimiento.
- Grupos de imágenes.
- Separar audio.
- Identificar grupos en monitoreo de salud.

##--
Para ahondar más en el tema es clave ese concepto de “similtud” y sus medidas. Tambien vale la pena mencionar que otro método muy usado que busca crear estos clusters , conglomerados o agrupaciones es KNN(K nearest neighbors)

##--
K means
Es un algoritmo no supervisado que consiste en agrupar los datos a partir de las similitudes que tenga.
Estos datos se agrupan alrededor de centroides (k centroides).
Para calcular el k adecuado recurrimos al viejo método de prueba y error.

Nota:
Existe un método gráfico conocido como el método del codo (elbow), en el que elegimos el punto de inflexión de la grafica de errores obtenidos en cada valor de k

##---

¿Qué es K-Means?
Crea K grupos a partir de un grupo de observaciones, lo elementos deben de tener similitudes.

Selecciona un valor para K (Centroides)
Asignamos cada uno de los elementos restante al centro mas cercano.
Asignamos cada punto punto a su centroide mas cercano
Repetimos paso 2 y 3 hasta que los centros no se modifiquen.
Método del codo

Lo que hace es dividir los siguiente centroides o información hasta graficarlo en un panel o un eje XY

Calcula el agrupamiento para diferentes de K

El error al cuadrado para cada punto es el cuadrado de las distancia del punto desde su centro.

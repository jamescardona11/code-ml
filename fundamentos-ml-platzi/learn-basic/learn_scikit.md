Scikit Learn
Scikit Learn es una biblioteca de Python que está conformada por algoritmos de clasificación, regresión, reducción de la dimensionalidad y clustering. Es una biblioteca clave en la aplicación de algoritmos de Machine Learning, tiene los métodos básicos para llamar un algoritmo, dividir los datos en entrenamiento y prueba, entrenarlo, predecir y ponerlo a prueba.

Importar biblioteca:
from sklearn import [modulo]

División del conjunto de datos para entrenamiento y pruebas:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

Entrenar modelo:
[modelo].fit(X_train, y_train)

Predicción del modelo:
Y_pred = [modelo].predict(X_test)

Matriz de confusión:
metrics.confusion_matrix(y_test, y_pred)

Calcular la exactitud:
metrics.accuracy_score(y_test, y_pred)

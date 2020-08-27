#LINEAR REGRESSION SIMPLE
#Created on Thu Aug 13 20:07:46 2020

#@author: zoro
#

#PreProcessing dataset
# import dataset
dataset = read.csv('Salary_Data.csv')

#Split dataset in two subset 'Testing' and 'Training'
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3) #SplitRatio = TRAIN
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#scaling values
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de regresion lineal simple con el conjunto de entrenamiento
#summary(regression)
regression = lm(formula = Salary ~ YearsExperience, training_set)

#Predecir resultados para el conjunto de testing
y_pred = predict(regression, newdata = testing_set)

#visualización datos
install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), colour= "red")+
  geom_line(aes(x = training_set$YearsExperience, y =  predict(regression, newdata = training_set)), color = "blue")+
  ggtitle("Salary vs Experience Years (Train)")+
  xlab("Year Experience")+
  ylab("Salary $")
















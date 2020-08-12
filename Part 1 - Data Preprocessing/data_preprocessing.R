#PreProcessing dataset
# import dataset
dataset = read.csv('Data.csv')

#Split dataset in two subset 'Testing' and 'Training'
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#scaling values
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])





















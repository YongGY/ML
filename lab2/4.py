def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation > 0.5 else 0.0
 
# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate):
    count_sum = 0
    epoch = 0
    weights = [0.0 for i in range(len(train[0]))]
    while (count_sum < 2):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
        #============================
        if sum_error == 0:
            count_sum = count_sum + 1
        #============================
        epoch = epoch + 1
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights
 
##===========================================================
#for row in dataset:
#	prediction = predict(row, weights)
#	print("Expected=%d, Predicted=%d" % (row[-1], prediction))    
##===========================================================

# Calculate weights
#NAND [0.2, -0.2, -0.1]
dataset = [[0,0,1], [0,1,1], [1,0,1], [1,1,0]]

#NOR
dataset1 = [[0,0,1], [0,1,0], [1,0,0], [1,1,0]]

l_rate = 0.1


dataset2 = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]


weights = train_weights(dataset, l_rate)
print(weights)

weights1 = train_weights(dataset1, l_rate)
print(weights1)

weights2 = train_weights(dataset2, l_rate)
print(weights2)

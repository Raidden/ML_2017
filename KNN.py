import pandas as pd
import math
import operator




def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


if __name__ == '__main__':
    df = pd.read_csv('iris.data', header=None)
    df.head()
    data1 = [1 , 3 ,4 , "a"]
    data2 =[1 , 3 , 4 , "b"]
    result = euclideanDistance(data1 , data2 , 3)

    trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
    testInstance = [5, 5, 5]
    k = 1
    neighbors = getNeighbors(trainSet, testInstance, 1)
    print(neighbors)

    xx = [[1,1,1,'a'] , [1,1,1,'b'],[1,1,1,'a']]
    getResponse(xx)
    print(result)
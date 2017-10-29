import csv
import random
import math
import operator
import matplotlib as plt

def loadDataset(filename, split, trainingSet=[], testSet=[]):


    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        dataset = list(reader)
        print(dataset)
        for x in range(len(dataset) -1 ):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
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
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


if __name__ == '__main__':
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset('iris.data', split, trainingSet, testSet)
    predictions = []
    #train_set = [[5, 6,'a'], [6, 3,'a'], [10, 1,'b'],
     #            [10, 6,'a'], [5, 10,'b'] , [5, 6,'a'], [6, 3,'a'],
      #           [1, 1,'b'], [10, 6,'a'], [5, 10,'b'] ,[5, 6,'a'],
       #          [6, 3,'a'], [10, 1,'b'], [10, 6,'a'], [5, 10,'b'] ,[5, 6,'a'],
        #         [6, 3,'a'], [10, 1,'b'], [10, 6,'a'], [5, 10,'b']]
    #test_set  = [[7, 9, "b"], [1, 8,"a"], [8, 4,"a"], [8, 7,"b"], [7, 8, "b"]]


    print
    ('Train set: ' + repr(len(trainingSet)))
    print
    ('Test set: ' + repr(len(testSet)))

    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], 3)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

    plt.plot(trainingSet[0][0] , 1)
    plt.show()
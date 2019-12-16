import random
import numpy as np

# max number of iterations before algorithm stops 
max_iterations = 10

# helper function to check if the algorithm should stop
def stopCondition(old, centroids, iterations):
    if iterations > max_iterations:
        print("stopped because max iterations")
        return True
    if np.array_equal(old, centroids):
        print("stopped because old = centroids")
        return True
    else:
        return False

# helper function to calculate distances for labels
def generateLabels(data, centroids):
    """
    for each data element,
        find the closest centroid
        label the element with the index of the closest centroid
    """
    labels = [] # indeces of associated centroids
    for elem in data:
        distances = []
        for cent in centroids:
            distances.append(np.linalg.norm(np.asarray(elem)-np.asarray(cent)))
        #print("distance" + str(distances))
        labels.append(distances.index(min(distances)))
    return labels

# helper function to update the centroids
def updateCentroids(data, labels, minimums, maximums):
    """
    for each centroid:
      find the data points associated with that label
      average each column of those points to get the new centroids
      
    params:
      data: given data points
      labels: indeces of associated centroids
      minimums: min used for reinitializing centroids
      maximums: max used for reinitializing centroids
    """
    newCentroids = []
    for i in range(0,len(labels)):
        # find the data associated data points
        associatedPoints = []
        for j in range(0,len(data)):
            if labels[j] == i:
                #print(str(labels[j]) + " matches " + str(i))
                associatedPoints.append(data[j])
        # if there are no associated points, reinitialize the centroid
        if len(associatedPoints) == 0:
            newCent = []
            for j in range(len(data[0])):
                newCent.append(random.uniform(minimums[j], maximums[j]))
            newCentroids.append(np.array( newCent) )
            print("newCentRANDOM"+str(newCent))
            continue
        # calculate centroid by averaging each column of the data points
        newCent = np.average(associatedPoints, axis=0)
        print("newCent"+str(newCent))
        newCentroids.append(newCent)
    #print("--newCentroids--")
    #print(newCentroids)
    return newCentroids

# cluster data using k centroids
def yinyang(data, k):
    """
    Cluster data points into labels and return centroids of clusters
    """
    # get the number of columns
    columns = len(data[0])
    # find the min and max value for each column
    minimums = np.min(data, axis=0)
    maximums = np.max(data, axis=0)
    
    # generate k random initial centroids
    centroids = []
    for i in range(k):
        cent = []
        for j in range(columns):
            cent.append(random.uniform(minimums[j], maximums[j]))
        centroids.append(cent)
    
    centroids = np.array( centroids ) # convert centroids list to np array
    iterations = 0
    old = None
    
    while not stopCondition(old, centroids, iterations):
        old = centroids
        
        labels = generateLabels(data, centroids)
        
        print("labels" + str(labels))        
        
        print(iterations)
        iterations += 1
        
        centroids = updateCentroids(data, labels, minimums, maximums)
        
    
    
    return centroids



        
# generate some test data
testData = []
for i in range(10):
    testElement = []
    for j in range(4):
        testElement.append(random.uniform(0.0, 50.0))
    testData.append(testElement)
print("--data--")
for elem in testData:
    print(elem)


result = yinyang(testData, 6)
print("---centroids---")
for each in result:
    print(each)

    
    
    

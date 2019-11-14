import time
from sklearn import cluster

"""
# read in kegg network data
keggData = []
with open("Relation Network (Directed).data") as fp:
  line = fp.readline()
  while line:
    valueList = line.split(",")
    # remove the first element from the list
    valueList.pop(0)
    valueList = [float(i) for i in valueList]
    keggData.append(valueList)
    line = fp.readline()
    
# run the full kmeans algorithm on the kegg network data
start_time = time.time()
full_kmeans = cluster.KMeans(algorithm = "full").fit(keggData)
print("Kegg Network Full :" + str(time.time() - start_time))

# run the elkan kmeans algorithm on the kegg network data
start_time = time.time()
elkan_kmeans = cluster.KMeans(algorithm = "elkan").fit(keggData)
print("Kegg Network Elkan :" + str(time.time() - start_time))

"""

# read in gas sensor data n = 445 d = 128
driftData = []
with open("driftdataset/batch1.dat") as fp:
  line = fp.readline()
  while line:
    valueList = line.split(" ")
    floatList = []
    # remove number in front of each element
    for each in valueList:
      each.replace(';', ':')
      values = each.split(":")
      values.pop(0)
      print(values)
      #floatList.append(values)
    floatList = [float(i) for i in valueList]
    driftData.append(floatList)
    line = fp.readline()

# run the full kmeans algorithm on the gas sensor data
start_time = time.time()
full_kmeans = cluster.KMeans(algorithm = "full").fit(driftData)
print("Gas Sensor Full :" + str(time.time() - start_time))

# run the elkan kmeans algorithm on the gas sensor data
start_time = time.time()
elkan_kmeans = cluster.KMeans(algorithm = "elkan").fit(driftData)
print("Gas Sensor Elkan :" + str(time.time() - start_time))

# read in road (3d spatial network)

import time
from sklearn import cluster

# read in kegg network (Relation Network directed) aac00010,26,43,2,7,1,211,3.222748815,3.230769231,0,0,1,4.125757576,1.653846154,27,0,0.076923077
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
    
print(keggData)

# read in gas sensor (driftdatabase)
driftData = []

# read in road (3d spatial network)

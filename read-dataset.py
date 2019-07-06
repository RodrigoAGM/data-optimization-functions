import csv
import functions
import data_analisis_functions

data = []
labels = []
species = []

#read data
with open('iris.csv') as csvfile:
    reader = csv.reader(csvfile)
    cols = [1,2,3,4]
    for row in reader:

        if(not labels):
            newRow = list(row[i] for i in cols)
            labels = newRow
        else:
            newRow = list(float(row[i]) for i in cols)
            data.append(newRow)
            species.append(row[5])

#nomralize columns
norm = functions.normalize(functions.getColumn(data,0))
functions.replaceColumn(data,norm,0)

norm = functions.normalize(functions.getColumn(data,1))
functions.replaceColumn(data,norm,1)

norm = functions.normalize(functions.getColumn(data,2))
functions.replaceColumn(data,norm,2)

norm = functions.normalize(functions.getColumn(data,3))
functions.replaceColumn(data,norm,3)

newData = data_analisis_functions.pcaFunction(data, 2)
print(newData)
print(data_analisis_functions.kmeans_centers(newData,3))
print(data_analisis_functions.kmeans_predict(newData,3,[[0.345, 0.121]]))
print(data_analisis_functions.knn_predict(newData,3,species,[[-0.623546310,-0.100313199]]))
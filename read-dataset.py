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
            newRow = [[i] for i in cols]
            labels = newRow
        else:
            newRow = [float(row[i]) for i in cols]
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

print(functions.leximax(data)[0])
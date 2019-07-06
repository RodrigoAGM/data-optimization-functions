import csv
import functions

data = []
labels = []

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
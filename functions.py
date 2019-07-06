def getColumn(data, i):
    return [row[i] for row in data]

def replaceColumn(data, newData, i):
    for pos in range(len(data)):
        data[pos][i] = newData[pos]

    return data

def normalize(data):
    """
    Data normalization function that gets a dataset readed as a list of lists
    and returns the same dataset with the normalized data.
    """
    minVal = min(data)
    maxVal = max(data)
    result = list(map(lambda x: (x - minVal) / (maxVal - minVal), data))
    return result

def WA(data,weights):
    """
    Function that gets a dataset readed as a list of lists and a list of weights for
    each column and returns the dataframe with the WA.
    """
    total = sum(weights)
    newData = []
    for row in data:
        val = 0
        for i in range(len(row)):
            val = val + ((row[i] * weights[i])/total)
        row.append(val)
        newData.append(row)
    return newData
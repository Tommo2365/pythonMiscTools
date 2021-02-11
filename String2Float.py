import numpy as np

def String2Float(csvData):
    #Find the numnber of rows of numeric data
    data = csvData
    
    numDataRows = np.shape(data)[0]
    numberCols = np.shape(data)[1]
    #Pull out the data
    
    
    dataArray = np.ones([numDataRows,numberCols])

    for k in range (0,numDataRows):
        for w  in range(0, numberCols):
            thisElement = data[k,w]
            isEmpty = not thisElement
            if(isEmpty==True):
                continue
            thisFloat = float(thisElement)
            dataArray[k,w] = thisFloat
    return dataArray
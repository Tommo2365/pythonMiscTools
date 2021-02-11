import numpy
import numpy as np
import matplotlib.pyplot as plt
import csv
from String2Float import String2Float
def CSVRead(fileName, bHeader, nHeaderRows):
    
    print('Loading File:    ' + fileName)

    #data = numpy.array([])
    listData = []
    #data = []

    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        #print(csv_reader)
        line_count = 0
        for row in csv_reader:
        # print(row)
            listData.append(row)
            #data = np.append(data, row)
            line_count += 1
        if(bHeader == True):
            # Assume the header is the first row, take the 2nd row to to end for the data
            csvData = np.array(listData[nHeaderRows:len(listData)])
            #csvData = csvData.astype('float')
            header =  np.array(listData[0:nHeaderRows])
        elif(bHeader == False):
            csvData = np.array(listData)
            try:
                csvData = csvData.astype('float')
            except:
                try:
                    csvData = String2Float(csvData)
                except:
                    return csvData


            header =  ''
        print(f'Processed {line_count} lines ' + 'arraySize ' + str(csvData.shape))
        # plt.imshow(csvData)
        # plt.colorbar()
        # plt.show()
        return csvData, header

    
    

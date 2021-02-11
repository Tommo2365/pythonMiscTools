# Create array from txt file

output = np.array([])

for index in range(0, nRows):
    thisElement = data[index] 
    #print(thisElement)
    splitString = thisElement.split('\n')   # \n = return
    valueString = splitString[0]
    #value = float(valueString)             # if float to string
    output = np.append(valueString,output)
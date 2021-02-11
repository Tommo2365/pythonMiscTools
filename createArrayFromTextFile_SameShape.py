
# Make array from txt file the same shape as input 'file = file.txt'

lc=0                                                            # Keep track of number of lines

for i in f:                                                     # The number of lines in 'f'
    lc+=1                                                       
file.seek(0)                                                    # Go back to line 0
print(" ")                                                      # Used to create a space in the shell
print("There are",lc,"lines in the file")                       # Prints the numbe of lines

darray=np.ndarray(shape=lc,dtype=float)                         # Declare and array 'lc' long

j=0                                                                         # Index of 'i'
for i in f:                                                                 # Stores each element in 'i' (Where 'i' is = to each line)
    darray[j]=float(i)                                                      # Turns each value for 'i' into a float and puts each line into an array
    j=j+1                                                                   # Keeps track of each line
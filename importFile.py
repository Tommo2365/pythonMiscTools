## Opens a window to select file from different directory

import os

path = r'C:\temp'
os.chdir(path)
print("Please select a .txt file..." )

infile = filedialog.askopenfilename()

## Check the file name and loaction after selecting

# print(os.getcwd())              # where is this file?
# print(os.listdir())             # list all the files in that directory




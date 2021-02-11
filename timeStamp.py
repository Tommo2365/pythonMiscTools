# Create a timestamp on the save file
import time
from datetime import datetime

now = datetime.now() 
timeStamp = now.strftime("%Y%m%d_%H_%M_%S_")
print(timeStamp)



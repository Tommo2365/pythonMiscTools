import numpy as np

## Save file as csv with name  = timestamp.
## fmt=['%s'] = 1 col
## fmt=['%s', '%s'] = 2 col

np.savetxt(timestamp + 'Data.csv', output, delimiter=',', fmt=['%s'], header=[])
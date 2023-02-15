
import numpy as np
import pandas as pd

f=pd.read_csv('s.csv')


f=f[f['Column1'] > 0]

np.savetxt('f.csv',f)


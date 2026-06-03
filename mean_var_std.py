import numpy as np
import pandas as pd

def calculate(m):
    if len(m) == 9:
        m = np.array(m).reshape(3,3)
        matrix = {'mean': [(m).mean(axis=0).tolist(), (m).mean(axis=1).tolist(), (m).mean()],
                  'variance': [(m).var(axis=0).tolist(), (m).var(axis=1).tolist(), (m).var()],
                  'standard deviation': [(m).std(axis=0).tolist(), (m).std(axis=1).tolist(), (m).std()],
                  'max': [(m).max(axis=0).tolist(), (m).max(axis=1).tolist(), (m).max()],
                  'min': [(m).min(axis=0).tolist(), (m).min(axis=1).tolist(), (m).min()],
                  'sum': [(m).sum(axis=0).tolist(), (m).sum(axis=1).tolist(), (m).sum()]
                  } 
        return matrix
    else:
        raise ValueError('List must contain nine numbers.')

l = [0,1,2,3,4,5,6,7,8]
x = calculate(l)
print(x)
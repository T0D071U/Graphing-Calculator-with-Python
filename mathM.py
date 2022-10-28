import numpy as np
from math import *

def graphList():
  list = []
  for x in np.arange(-100.0, 100.0, 0.1):
    y = 5*x** 2
    cords = [x, y] 
    list += [cords]
  print(len(list))
  return list
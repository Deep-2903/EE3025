import numpy as np

''' The following fuction adds two polynomials defined by vectors x and y 
z = add(x,y) '''

def add(x,y):
  m = len(x)
  n = len(y)

  if m == n:
    z = x + y

  elif m > n:
    z = np.array((np.zeros(m-n),y)) + x

  else:
    z = np.array((np.zeros(n-m),x)) + y

    return z

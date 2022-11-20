import numpy as np
import matplotlib.pyplot as plt
from classes import TriGrid,Quadrature,Basis
from StationaryProblem import StationaryProblem

# base = Basis(3)
# base.plotPhi(3)

A = np.array([1, 2, 3,4 ,5 ,6,7 ,9 ,12])
index = np.array([0, 8])
print(A[index])
f = lambda x: x
A[index] = f(np.array([0, 8]))
print(A)



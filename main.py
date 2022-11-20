import numpy as np
import matplotlib.pyplot as plt
from classes import TriGrid,Quadrature,Basis
from StationaryProblem import StationaryProblem
from timeStepping import timeStep


grid = TriGrid(0,0.1,10)
quadrature = Quadrature(2)
basis = Basis()
f = lambda x: 0
g = lambda x: x
a = lambda x: 1/1000
b = lambda x: np.array([-10])

pde = StationaryProblem(grid,basis,quadrature,lambda x: True,g)
pde.addSource(f)
pde.addDiffusion(a)
pde.addConvection(b)
# pde.addM()

pde.solve()
pde.show()

# I = lambda x: np.exp(-(x-0.5)**2/0.01)
# U0 = grid.points[:,0]
# U0 = np.ones(np.shape(grid.points)[0])

# time = timeStep(pde,U0,10)
# time.solve()



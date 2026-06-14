from DistrictLogic import Cell
import numpy as np

p = [np.array([-1, -1]), np.array([1, 1])]
texas = Cell(np.array([1.5, -2.0]), np.array([[4, 1.2], [1.2, 3]]), 500)
texas.assign_votes(p)
print(texas.votes)
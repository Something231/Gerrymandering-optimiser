from DistrictLogic import Cell
import numpy as np
import random

random.seed(67)
np.random.seed(67)
#political alignment is to go from +- 10 in all directions
sizeX = 10
sizeY = 10
p = [np.array([-1, -1]), np.array([1, 1])]


map = np.empty((sizeY, sizeX), dtype=object)
for y in range(sizeY):
    for x in range(sizeX):
        stdx = np.random.uniform(1, 3)
        stdy = np.random.uniform(1, 3)
        rot = np.random.uniform(-0.5, 0.5)
        map[y][x] = Cell(np.array([random.uniform(-9, 9), random.uniform(-9, 9)]), np.array([[stdx**2, stdx*stdy*rot], [stdy*stdx*rot, stdy**2]]), 500)
        map[y][x].assign_votes(p)

print(map)
texas = Cell(np.array([1.5, -2.0]), np.array([[4, 1.2], [1.2, 3]]), 500)
texas.assign_votes(p)
print(texas.votes)
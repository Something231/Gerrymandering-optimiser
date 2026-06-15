from DistrictLogic import Cell
import numpy as np
import random
import matplotlib.pyplot
import matplotlib.patches

#random.seed(67)
#np.random.seed(67)

#political alignment is to go from +- 10 in all directions
sizeX = 10
sizeY = 10
p = [np.array([-1, -1]), np.array([1, 1])]
est_tally = [0, 0]
e_size = 5

fig, ax = matplotlib.pyplot.subplots()

map = np.empty((sizeY, sizeX), dtype=object)
for y in range(sizeY):
    for x in range(sizeX):
        stdx = np.random.uniform(1, 3)
        stdy = np.random.uniform(1, 3)
        rot = np.random.uniform(-0.5, 0.5)
        map[y][x] = Cell(np.array([random.uniform(-9, 9), random.uniform(-9, 9)]), np.array([[stdx**2, stdx*stdy*rot], [stdy*stdx*rot, stdy**2]]), 500)
        map[y][x].assign_votes(p)
        map[y][x].affiliate()
        c = 'green'
        if map[y][x].affiliation == 1:
            c = 'orange'
            est_tally[0] += 1
        else:
            est_tally[1] += 1
        ax.add_patch(matplotlib.patches.Rectangle((x, y), 1, 1, color=c))

ax.set_ylim(sizeY)
ax.set_xlim(sizeX)
matplotlib.pyplot.savefig("districts.png")
print('Saved!')
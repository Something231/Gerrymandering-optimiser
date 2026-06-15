import numpy as np
from math import ceil

def verify_possible(districts, est_tally, e_size, w) -> bool:  #quick check to see weather it is reasonably doable, will miss some chances but whatever
    size = districts.shape
    t = size[0]*size[1]
    n = int(t/e_size)
    if est_tally[w] >= ((ceil(0.51 * n)/n) * (ceil(0.51 * e_size)/e_size) * t):
        return True
    else:
        return False

def simple_attempt(districts):
    s = districts.shape
    simplified = np.zeros(s)
    for y in range(s[0]):
        for x in range(s[1]):
            simplified[y][x] = districts[y][x].affiliation
    pass #to add a 'packing/cracking' algorithm but need time to think how
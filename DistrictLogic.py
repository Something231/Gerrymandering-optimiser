import numpy as np

#mean is a 2d vector, covariance is a 2x2 matrix
class Cell:
    def __init__(self, mean, covariance, population:int):
        self.mean = mean
        self.covariance = covariance
        self.population:int = population
        self.people = np.random.multivariate_normal(self.mean, self.covariance, self.population)
        self.explode = True
        self.votes:list

    def assign_votes(self, parties):
        self.votes = [0] * len(parties)
        for p in self.people:
            closest_distance = float(99999.9)
            closest_id = None
            for n, q in enumerate(parties):
                d = np.linalg.norm(q - p)
                if d == closest_distance:
                    exit() #idk what to do here yet
                elif d < closest_distance:
                    closest_distance = d
                    closest_id = n
            self.votes[closest_id] += 1

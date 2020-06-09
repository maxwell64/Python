import numpy as np
from numpy.random import default_rng
rng = default_rng()


class Mol:
    def __init__(self):
        # Initialises a new Mol with start position and random velocity vector
        self.pos = [500, 500]
        self.vel = list(rng.standard_normal(2))
        self.mutation_count = 0
        self.fitness = 0

    def mutate(self):
        # Randomises the velocity of the Mol
        self.vel = list(rng.standard_normal(2))

    def update(self):
        # Updates the position of the Mol and mutates if conditions are met
        mutation_factor = np.random.random()
        if mutation_factor < 0.01:
            self.mutate()
            self.mutation_count += 1
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def measure_fitness(self, goal):
        xdiff = goal[0] - self.pos[0]
        ydiff = goal[1] - self.pos[1]
        self.fitness = np.sqrt(xdiff**2 + ydiff**2)

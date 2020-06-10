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
        self.memory = []
        self.is_dead = False

    def mutate(self):
        # Randomises the velocity of the Mol
        self.vel = list(rng.standard_normal(2))

    def remember(self, i):
        if len(self.memory) <= i:
            self.memory.append(self.vel)
        else:
            self.memory[i] = self.vel

    def kill(self, bounds):
        if self.pos[0] >= bounds[0] or self.pos[1] >= bounds[1]:
            self.is_dead = True

    def update(self, i, bounds):
        # Updates the position of the mol and mutates if conditions are met
        # Also saves the velocity of the mol to memory
        if not self.is_dead:
            mutation_factor = np.random.random()
            if len(self.memory) <= i:
                if mutation_factor < 0.01:
                    self.mutate()
                    self.mutation_count += 1
            else:
                self.vel[0] = self.memory[i][0]
                self.vel[1] = self.memory[i][1]
                if mutation_factor < 0.01:
                    self.mutate()
                    self.mutation_count += 1
            self.remember(i)
            self.kill(bounds)
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]

    def measure_fitness(self, goal):
        # Calculates the fitness (distance from goal) of the mol at finish
        xdiff = goal[0] - self.pos[0]
        ydiff = goal[1] - self.pos[1]
        self.fitness = np.sqrt(xdiff**2 + ydiff**2)

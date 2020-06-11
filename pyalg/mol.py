import numpy as np
from numpy.random import default_rng
rng = default_rng()
# Initialises the random number generator


class Mol:
    def __init__(self):
        # Initialises a new mol with start position and random velocity vector
        # Also presets a few important parameters for later
        self.pos = [500, 500]
        self.vel = list(rng.standard_normal(2))
        self.mutation_count = 0
        self.fitness = 0
        self.memory = []
        self.is_dead = False
        self.is_best = False

    def mutate(self):
        # Randomises the velocity of the mol
        self.vel = list(rng.standard_normal(2))

    def remember(self, i):
        # Saves the velocities to the memory of the mol
        if len(self.memory) <= i:
            self.memory.append(self.vel)
        else:
            self.memory[i] = self.vel

    def kill(self, bounds):
        # Kills the mol if it escapes the area
        if self.pos[0] >= bounds[0] or self.pos[1] >= bounds[1]:
            self.is_dead = True
        if self.pos[0] <= 0 or self.pos[1] <= 0:
            self.is_dead = True

    def update(self, i, bounds):
        # Updates the position of the mol and mutates if conditions are met
        # Also calls the remember function
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
        xdiff = 1 / np.abs(self.pos[0] - goal[0])
        ydiff = 1 / np.abs(self.pos[1] - goal[1])
        self.fitness = np.sqrt(xdiff**2 + ydiff**2) ** 3

    def clone(self):
        new_mol = Mol()
        new_mol.memory = self.memory
        return new_mol

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
        self.reached_goal = False

    def mutate(self):
        # Randomises the velocity of the mol
        if not self.is_best:
            self.vel = list(rng.standard_normal(2))

    def remember(self, i):
        # Saves the velocities to the memory of the mol
        if len(self.memory) <= i:
            self.memory.append(self.vel)
        else:
            self.memory[i] = self.vel

    def kill(self, bounds, goal):
        # Kills the mol if it escapes the area
        if self.pos[0] >= bounds[0] or self.pos[1] >= bounds[1]:
            self.is_dead = True
        if self.pos[0] <= 0 or self.pos[1] <= 0:
            self.is_dead = True
        if self.pos[0] == goal[0] and self.pos[1] == goal[1]:
            self.is_dead = True
            self.reached_goal = True

    def update(self, i, bounds, goal):
        # Updates the position of the mol and mutates if conditions are met
        # Also calls the remember function and determines if the mol is dead
        if not self.is_dead:
            mutation_factor = np.random.random_sample()
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
            self.kill(bounds, goal)
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]

    def measure_fitness(self, goal):
        # Calculates the fitness (distance from goal) of the mol at finish
        xdiff = np.abs(self.pos[0] - goal[0])
        ydiff = np.abs(self.pos[1] - goal[1])
        self.fitness = 1 / (xdiff**2 + ydiff**2)
        if self.reached_goal:
            self.fitness += 2

    def clone(self):
        # Returns a clone with the memories of the mol
        new_mol = Mol()
        new_mol.memory = self.memory
        if self.is_best:
            new_mol.is_best = True
        return new_mol

import numpy as np

class Brain:

    def __init__(self,size):

        self.size = size
        self.memory = []
        self.step = 0
        self.mutationRate = 0.01

        self.randomise()

    def randomise(self):
        for i in range(self.size):
            self.memory.append(np.array([np.random.randint(0,5),np.random.randint(0,5)]))

    def clone(self):
        clone = Brain(1000)
        for i in range(len(self.memory)):
            clone.memory[i] = self.memory[i]
        return clone

    def mutate(self):
        for i in self.memory:
            rand = np.random.random([0,1])
            if rand < self.mutationRate:
                i = np.array([np.random.randint([0,5]),np.random.randint([0,5])])

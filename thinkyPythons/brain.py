import numpy as np

class Brain:

    def __init__(self,size):

        self.size = size
        self.memory = []
        self.step = 0
        self.mutationRate = 0.05

    def randomise(self):
        for i in range(self.size):
            self.memory.append(np.array([np.random.randint(-5,5),np.random.randint(-5,5)]))

    def clone(self):
        clone = Brain(len(self.memory))
        for i in range(len(self.memory)):
            clone.memory.append(self.memory[i])
        return clone

    def mutate(self):
        for i in self.memory:
            rand = np.random.random_sample()
            if rand < self.mutationRate:
                i = np.array([np.random.randint(-5,5),np.random.randint(-5,5)])

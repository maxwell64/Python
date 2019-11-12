from brain import Brain
import numpy as np
width = 500
height = 500
goalPos = np.array([250,20])

class Player:

    def __init__(self):

        self.pos = np.array([width/2,7*height/8])
        self.acc = np.array([0,0])
        self.dead = False
        self.reachedGoal = False
        self.fitness = 0
        self.brain = Brain(400)
        self.brain.randomise()

    def update(self):
        while (len(self.brain.memory) > self.brain.step):
            self.acc = self.brain.memory[self.brain.step]
            self.brain.step += 1
            self.pos = np.add(self.pos,self.acc)
            if (self.pos[0] == goalPos[0] and self.pos[1] == goalPos[1]):
                self.reachedGoal = True
            if (self.pos[0] >= width or self.pos[0] <= 0 or self.pos[1] >= height or self.pos[1] <= 0 or self.brain.step >= self.brain.size):
                self.dead = True

    def calculateFitness(self):
        if self.reachedGoal == True:
            self.fitness = 1.0 / (16.0 * 1000.0 / float(brain.step ** 2))
        else:
            self.distanceToGoal = np.abs(np.sum(np.dot(goalPos,self.pos)))
            self.fitness = 1.0 / (self.distanceToGoal ** 2)

    def clonePlayer(self):
        temp = Player()
        temp.brain = self.brain.clone()
        return temp

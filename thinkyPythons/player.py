from brain import Brain
import numpy as np
width = 1000
height = 1000
goalPos = np.array([500,20])

class Player:

    def __init__(self):

        self.pos = np.array([width/2,height/8])
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])
        self.dead = False
        self.reachedGoal = False
        self.isBest = False
        self.fitness = 0
        self.brain = Brain(200)

    def update(self):
        if (len(self.brain.memory) > self.brain.step):
            acc = self.brain.memory[brain.step]
            self.brain.step += 1
        vel = np.add(vel,acc)
        pos = np.add(pos,vel)
        self.brain.step += 1

        if (self.pos[0] == goal[0] and self.pos[1] == goal[1]):
            self.reachedGoal = True
        if (self.pos[0] > width or self.pos[0] < 0 or self.pos[1] > height or self.pos[1] < 0 or brain.step > brain.size):
            self.dead = True

    def calculateFitness(self):
        if self.reachedGoal:
            self.fitness = 1.0 / (16.0 * 1000.0 / float(brain.step * brain.step))
        else:
            self.distanceToGoal = np.sum(np.subtract(goalPos,self.pos))
            self.fitness = 1.0 * (self.distanceToGoal ** 2)

    def clonePlayer(self):
        temp = Player()
        temp.brain = self.brain.clone()
        return temp

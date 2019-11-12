import numpy as np

from player import Player
from brain import Brain

class Population:

    def __init__(self,totalPlayers):

        self.players = []
        self.fitnessSum = 0
        self.generation = 1
        self.allDead = False
        self.bestFitness = 0

        for i in range(totalPlayers):
            temp = Player()
            self.players.append(temp)

    def updateAll(self):
        for i in self.players:
            if (i.dead != True and i.reachedGoal != True):
                i.update()

    def selectBest(self):
        for i in self.players:
            if i.fitness > self.bestFitness:
                self.bestPlayer = i
                self.bestFitness = self.bestPlayer.fitness

    def checkAllDead(self):
        for i in self.players:
            if i.dead != True:
                self.allDead = False
        self.allDead = True

    def calculateFitness(self):
        for i in self.players:
            i.calculateFitness()
            self.fitnessSum += i.fitness

    def naturalSelection(self):
        newPlayers = []
        newPlayers.append(self.bestPlayer.clonePlayer())
        while len(newPlayers) < len(self.players):
            parent = self.selectParent()
            clone = parent.clonePlayer()
            clone.dead = False
            newPlayers.append(clone)
        self.players = newPlayers
        self.mutants()
        self.generation += 1

    def selectParent(self):
        rand = np.random.uniform(0,self.fitnessSum)
        runningSum = 0
        for i in self.players:
            runningSum += i.fitness
            if runningSum > rand:
                return i
        return None

    def mutants(self):
        for i in self.players:
            i.brain.mutate()

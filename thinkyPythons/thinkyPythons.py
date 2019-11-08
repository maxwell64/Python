import numpy as np
from population import Population
from brain import Brain
from player import Player

height = 1000
width = 1000
goalPos = np.array([500,20])

test = Population(200)
while test.generation < 1000:
    if (test.allDead != True):
        test.updateAll()
        test.checkAllDead()
    else:
        test.calculateFitness()
        print(test.fitnessSum)
        test.selectBest()
        print(test.bestFitness)
        print(test.bestPlayer.distanceToGoal)
        test.naturalSelection()
        test.mutants()
        test.fitnessSum = 0
        test.checkAllDead()

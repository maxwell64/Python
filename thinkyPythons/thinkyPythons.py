import numpy as np
from population import Population
from brain import Brain
from player import Player

height = 1000
width = 1000
goalPos = np.array([500,20])

test = Population(200)
while test.generation < 1000:
    test.checkAllDead()
    print(test.generation)
    if (test.allDead != True):
        test.updateAll()
    else:
        test.calculateFitness()
        print(test.fitnessSum)
        test.selectBest()
        print(test.bestFitness)
        print(test.bestPlayer.distanceToGoal)
        test.naturalSelection()
        test.mutants()
        test.generation += 1
        test.fitnessSum = 0

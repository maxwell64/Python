import numpy as np
from population import Population
from brain import Brain
from player import Player

height = 1000
width = 1000
goalPos = np.array([500,20])

test = Population(200)
while test.generation < 1000:
    while (test.allDead != True):
        test.updateAll()
        test.checkAllDead()
    test.calculateFitness()
    print(test.fitnessSum)
    test.selectBest()
    print(test.bestPlayer.distanceToGoal)
    print(test.generation)
    test.naturalSelection()
    test.fitnessSum = 0
    test.allDead = False

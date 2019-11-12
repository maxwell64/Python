import numpy as np
from population import Population
from brain import Brain
from player import Player

height = 500
width = 500
goalPos = np.array([250,20])

test = Population(20)
while test.generation < 100:
    print(test.generation)
    while (test.allDead != True):
        test.updateAll()
        test.checkAllDead()
    test.calculateFitness()
    print(test.fitnessSum)
    test.selectBest()
    test.naturalSelection()
    test.allDead = False

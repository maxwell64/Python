from mol import Mol
import numpy as np


# Initial parameters for the algorithm
dimensions = [1000, 1000]
population_size = 100
lifetime = 1000
goal = [999, 999]
generation = 0


def create_population(size):
    # Returns a population of mols to test
    population = []
    for i in range(size):
        temp = Mol()
        population.append(temp)

    return population


def run(pop):
    step = 0
    fitness_sum = 0
    global fitness_average
    while step < lifetime:
        for i in pop:
            i.update(step, dimensions)
        step += 1
    for i in pop:
        i.measure_fitness(goal)
        fitness_sum += i.fitness
    fitness_average = fitness_sum / population_size


def main():
    population = create_population(population_size)
    run(population)
    print(population[99].mutation_count)
    print(population[99].pos)
    print(population[99].vel)
    print(population[99].is_dead)


if __name__ == "__main__":
    main()

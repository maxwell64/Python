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
    # Runs the full test and computes the fitness of the mols
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
    select_best(pop)


def select_best(pop):
    # Finds the mol with the highest fitness value
    best_fitness = 0
    global best
    for i in pop:
        if i.fitness > best_fitness:
            best_fitness = i.fitness
            best = i


def main():
    population = create_population(population_size)
    run(population)
    print(best.mutation_count)
    print(best.is_dead)
    print(best.pos)
    print(best.fitness)
    print(fitness_average)


if __name__ == "__main__":
    main()

from mol import Mol
import numpy as np


# Initial parameters for the algorithm
dimensions = [1000, 1000]
population_size = 100
lifetime = 1000
goal = [999, 999]
iterations = 100


def create_population(size):
    # Returns a population of mols to test
    population = []
    while len(population) < size:
        temp = Mol()
        population.append(temp)
    return population


def run(pop):
    # Runs the full test and computes the fitness of the mols
    global generation
    generation = 0
    group = pop
    while generation < iterations:
        step = 0
        global fitness_sum
        fitness_sum = 0
        global fitness_average
        while step < lifetime:
            for i in group:
                i.update(step, dimensions)
            step += 1
        for i in pop:
            i.measure_fitness(goal)
            fitness_sum += i.fitness
        fitness_average = fitness_sum / population_size
        select_best(group)
        print(best.mutation_count)
        print(best.is_dead)
        print(best.pos)
        print(best.fitness)
        print(fitness_average)
        print(len(group))
        group = improve(group)
        generation += 1


def select_best(pop):
    # Finds the mol with the highest fitness value
    best_fitness = 0
    global best
    for i in pop:
        if i.fitness > best_fitness:
            best_fitness = i.fitness
            best = i


def select_parent(pop):
    # Selects the mols to clone for the next generation, based on fitness
    running_sum = 0
    rand = np.random.uniform(0, fitness_sum)
    for i in pop:
        running_sum += i.fitness
        if running_sum >= rand:
            new = i.clone()
            return new


def improve(pop):
    # Produces the next generation of mols based on the fittest previous
    next_generation = []
    next_generation.append(best)
    while len(next_generation) < population_size:
        temp = select_parent(pop)
        next_generation.append(temp)
    return next_generation


def main():
    # Runs all the things
    population = create_population(population_size)
    run(population)


if __name__ == "__main__":
    main()

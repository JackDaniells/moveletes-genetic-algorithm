import Population, Trajectory, GeneticAlgorithm

import datetime

POPULATION_SIZE = 1000
INDIVIDUAL_SIZE = 100
ELITE_SIZE = 1000
MUTATION_RATE = 0.01
GENERATIONS = 1000


print("[" + str(datetime.datetime.now()) + "] " + "Program started!")



#le as trajetorias
print("[" + str(datetime.datetime.now()) + "] " + "Reading files...")

trajectories = Trajectory.read()

print("[" + str(datetime.datetime.now()) + "] " + "Trajectories found: " + str(len(trajectories)))

# for t in trajectories:
#     print(t)



#cria os individuos
print("[" + str(datetime.datetime.now()) + "] " + "Creating population...")

pop = Population.create(trajetories=trajectories, individualSize=INDIVIDUAL_SIZE, populationSize=POPULATION_SIZE)

print("[" + str(datetime.datetime.now()) + "] " + "Population size: " + str(len(pop)))


#instancia o algoritmo genetico
print("[" + str(datetime.datetime.now()) + "] " + "Running Genetic Algorithm...")
print("[" + str(datetime.datetime.now()) + "] " + "Generations: " + str(GENERATIONS))

GeneticAlgorithm.run(population=pop, eliteSize=ELITE_SIZE, mutationRate=MUTATION_RATE, generations=GENERATIONS)

print("[" + str(datetime.datetime.now()) + "] " + "Program completed!")




import Population, Trajectory, GeneticAlgorithm

import datetime

print("[" + str(datetime.datetime.now()) + "] " + "program started")



#le as trajetorias
print("[" + str(datetime.datetime.now()) + "] " + "Reading files...")

trajectories = Trajectory.read()

print("[" + str(datetime.datetime.now()) + "] " + "Trajectories found: " + str(len(trajectories)))

# for t in trajectories:
#     print(t)



#cria os individuos
print("[" + str(datetime.datetime.now()) + "] " + "Creating population...")

pop = Population.create(trajetories=trajectories, size=4, popSize=10)

print("[" + str(datetime.datetime.now()) + "] " + "Population size: " + str(len(pop)))


#instancia o algoritmo genetico
GeneticAlgorithm.run(population=pop, eliteSize=10, mutationRate=0.01, generations=1)




import Population, Trajectory, GeneticAlgorithm


filePath = "../datasets/E1/1_patel_hurricane_2vs3/train"

#le as trajetorias
trajectories = Trajectory.readFiles(filePath)

#cria os individuos
pop = Population.create(trajetories=trajectories, size=10, qty=50)

print(len(pop))

#instancia o algoritmo genetico
GeneticAlgorithm.run(population=pop, popSize=10, eliteSize=5, mutationRate=0.01, generations=500)




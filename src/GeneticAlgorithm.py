
from src import MatingPool, Fitness

import datetime

# roda o AG
def run(population, eliteSize, mutationRate, generations, trajectories):

    gen = population
    
    for i in range(0, generations):

        print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i))

        gen = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)

        # print('.', end='', flush=True)

    print('')

# def runPlot(population, popSize, eliteSize, mutationRate, generations):
    
#     progress = []
    
#     for i in range(0, generations):
        
#         print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i))

#         gen = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)
    
#     plt.plot(progress)
#     plt.ylabel('Fitness')
#     plt.xlabel('Generation')
#     plt.show()


# crias as novas gerações da população
def nextGeneration(currentGen, eliteSize, mutationRate, trajectories):

    # rankeia os individuos
    popRanked = Fitness.rankPopulation(population=currentGen, trajectories=trajectories)

    # seleciona os melhores para  reprodução
    selectionResults = Fitness.selection(popRanked=popRanked, eliteSize=eliteSize)

    # faz o crossover entre os individuos
    children = MatingPool.breedPopulation(matingpool=selectionResults)

    # faz a mutação dos indivíduos
    nextGeneration = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate)
    
    return nextGeneration
    
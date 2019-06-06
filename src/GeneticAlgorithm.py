
from src import MatingPool, Fitness

import matplotlib.pyplot as plt

import datetime

# roda o AG
def run(population, eliteSize, mutationRate, generations, trajectories):

    gen = population
    
    for i in range(0, generations):

        print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i))

        gen = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)

        # print('.', end='', flush=True)

    print('')

def runPlot(population, eliteSize, mutationRate, generations, trajectories):
    
    progress = []

    gen = population

    
    for i in range(0, generations):
        
        print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i))

        gen = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)


        betterScore = 0
        for i in gen:
            if i.score > betterScore:
                betterScore = i.score
        
        progress.append(betterScore)

    
    plt.plot(progress)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.show()


# crias as novas gerações da população
def nextGeneration(currentGen, eliteSize, mutationRate, trajectories):

    # rankeia os individuos
    popRanked = Fitness.rankPopulation(population=currentGen, trajectories=trajectories)
    print(popRanked[0].score)

    # seleciona os melhores para reprodução
    selectionResults = Fitness.selection(popRanked=popRanked, eliteSize=eliteSize)

    # faz o crossover entre os individuos
    children = MatingPool.breedPopulation(matingpool=selectionResults, eliteSize=eliteSize)

    # faz a mutação dos indivíduos
    nextGeneration = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate)
    
    return nextGeneration
    
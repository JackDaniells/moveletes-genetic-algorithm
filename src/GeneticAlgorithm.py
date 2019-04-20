
import MatingPool, Fitness

# roda o AG
def run(population, eliteSize, mutationRate, generations):

    gen = population
    
    for i in range(0, generations):

        gen = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate)

        print('.', end='', flush=True)

    print('')


# crias as novas gerações da população
def nextGeneration(currentGen, eliteSize, mutationRate):

    # rankeia os individuos
    popRanked = Fitness.rankPopulation(population=currentGen)

    # seleciona os melhores para  reprodução
    selectionResults = Fitness.selection(popRanked=popRanked, eliteSize=eliteSize)

    # faz o crossover entre os individuos
    children = MatingPool.breedPopulation(matingpool=selectionResults)

    # faz a mutação dos indivíduos
    nextGeneration = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate)
    
    return nextGeneration
    
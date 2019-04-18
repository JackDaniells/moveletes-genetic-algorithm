
import Breed, Fitness, Individual, MatingPool, Mutate, Population

def run(population, popSize, eliteSize, mutationRate, generations):

    pop = Population.initialPopulation(popSize, population)
    
    for i in range(0, generations):

        pop = nextGeneration(pop, eliteSize, mutationRate)


def nextGeneration(currentGen, eliteSize, mutationRate):

    popRanked = Fitness.rankRoutes(currentGen)

    selectionResults = MatingPool.selection(popRanked, eliteSize)

    matingpool = MatingPool.matingPool(currentGen, selectionResults)

    children = Breed.breedPopulation(matingpool, eliteSize)

    nextGeneration = Mutate.mutatePopulation(children, mutationRate)
    
    return nextGeneration
    
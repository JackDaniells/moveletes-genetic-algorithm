
from src import Population

import random

import datetime

def breedIndividual(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1.movelets))
    geneB = int(random.random() * len(parent1.movelets))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1.movelets[i])
        
    childP2 = [item for item in parent2.movelets if item not in childP1]

    child = childP1 + childP2

    del childP1, childP2

    movelets = child
    return Population.Individual(movelets=movelets, score=0)


def breedPopulation(matingpool, eliteSize):

    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breedIndividual(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    
    return children



# mutação

def mutateIndividual(individual, mutationRate):

    print ('Mutating individual!')

    mutatePos = random.randrange(0, len(individual.movelets))

    oldMovelet = individual.movelets[mutatePos]

    newMovelet = Population.Movelet(trajectory=oldMovelet.trajectory, start=oldMovelet.start, size=oldMovelet.size, minSize=oldMovelet.minSize, maxSize=oldMovelet.maxSize)

    newMovelet.mutate()

    individual.movelets[mutatePos] = newMovelet


    #  zera o score do individuo
    individual.cleanScore()

    # percorre os movelets no individuo
    # for swapped in individual.movelets:
        # if(random.random() < mutationRate):
            # swapped.mutate()
            

    return individual


def mutatePopulation(population, mutationRate):
    
    mutatedPop = []
    
    for individual in population:

        if(random.random() < mutationRate):
            mutatedInd = mutateIndividual(individual=individual, mutationRate=mutationRate)
        else:
            mutatedInd = individual

        mutatedPop.append(mutatedInd)
        
    return mutatedPop
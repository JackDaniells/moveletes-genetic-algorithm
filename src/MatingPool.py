
from src import Population

import random

import datetime

def breedIndividual(parent1, parent2, trajectories):
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

    diffLength = len(parent1.movelets) - len(child)
    
    # if diffLength != 0:
    #     print('=======================================')
    #     print('individuo com tamanho diferente do original')
    #     print('=======================================')
    #     for i in range(0, diffLength):
    #         child.append(Population.createRandomMovelet(trajectories, parent1.movelets[0].minSize, parent1.movelets[0].maxSize))

    del childP1, childP2

    movelets = child
    return Population.Individual(movelets=movelets, score=0)


def breedPopulation(matingpool, eliteSize, trajectories):

    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breedIndividual(pool[i], pool[len(matingpool)-i-1], trajectories)
        children.append(child)
    
    return children



# mutação

def mutateIndividual(individual, mutationRate, trajectories):

    # print ('Mutating individual!')

    mutatePos = random.randrange(0, len(individual.movelets))

    oldMovelet = individual.movelets[mutatePos]

    # muta o movelet existente
    # newMovelet = Population.Movelet(trajectory=oldMovelet.trajectory, start=oldMovelet.start, size=oldMovelet.size, minSize=oldMovelet.minSize, maxSize=oldMovelet.maxSize)
    # newMovelet.mutate()

    # gera um novo movelet
    newMovelet = Population.createRandomMovelet(trajectories, oldMovelet.minSize, oldMovelet.maxSize)

    individual.movelets[mutatePos] = newMovelet

    #  zera o score do individuo
    individual.cleanScore()

    # percorre os movelets no individuo
    # for swapped in individual.movelets:
        # if(random.random() < mutationRate):
            # swapped.mutate()
            

    return individual


def mutatePopulation(population, mutationRate, eliteSize, trajectories):
    
    mutatedPop = []

    length = len(population)

    for i in range(0,eliteSize):
        mutatedPop.append(population[i])
    
    for i in range(eliteSize, length):

        individual = population[i]

        if(random.random() < mutationRate):
            mutatedInd = mutateIndividual(individual=individual, mutationRate=mutationRate, trajectories=trajectories)
        else:
            mutatedInd = individual

        mutatedPop.append(mutatedInd)
        
    return mutatedPop
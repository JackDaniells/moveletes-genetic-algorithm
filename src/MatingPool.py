
from src import Population

import random

#TODO: revisar
# def breedIndividual(parent1, parent2):

#     ind1 = []

#     ind2 = []

#     #  define o ponto de corte
#     splitPoint = random.randrange(parent1.size() - 1)
#     # splitPoint = int(parent1.size() / 2)

#     for i in range(parent1.size()):

#         if i < splitPoint:

#             ind1.append(parent1.movelets[i])
#             ind2.append(parent2.movelets[i])

#         else:

#             ind1.append(parent2.movelets[i])
#             ind2.append(parent1.movelets[i])


#     return Population.Individual(ind1), Population.Individual(ind2)
#     return parent1, parent2

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
    return  Population.Individual(child)


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

    # percorre os movelets no individuo
    for swapped in individual.movelets:

        if(random.random() < mutationRate):
            
            swapped.mutate()

            #  zera o score do individuo

    return individual


def mutatePopulation(population, mutationRate):
    
    mutatedPop = []
    
    for individual in population:

        mutatedInd = mutateIndividual(individual=individual, mutationRate=mutationRate)

        mutatedPop.append(mutatedInd)
        
    return mutatedPop

from src import Population

import random

#TODO: revisar
def breedIndividual(parent1, parent2):

    ind1 = {
        'movelets': [],
        'data': []
    }

    ind2 = {
        'movelets': [],
        'data': []
    }

    for j in range(0, len(parent2.dataMatrix['classes'])):

        ind1['data'].append([])
        ind2['data'].append([])

    #  define o ponto de corte
    splitPoint = random.randrange(parent1.size() - 1)
    # splitPoint = int(parent1.size() / 2)

    for i in range(parent1.size()):

        if i < splitPoint:

            ind1['movelets'].append(parent1.movelets[i])
            ind2['movelets'].append(parent2.movelets[i])

            for j in range(0, len(parent2.dataMatrix['classes'])):

                ind1['data'][j].append(parent1.dataMatrix['data'][j][i])
                ind2['data'][j].append(parent2.dataMatrix['data'][j][i])

        else:

            ind1['movelets'].append(parent2.movelets[i])
            ind2['movelets'].append(parent1.movelets[i])

            for j in range(0, len(parent2.dataMatrix['classes'])):
                ind1['data'][j].append(parent2.dataMatrix['data'][j][i])
                ind2['data'][j].append(parent1.dataMatrix['data'][j][i])


    parent1.movelets = ind1['movelets']
    parent1.dataMatrix['data'] = ind1['data']

    parent2.movelets = ind2['movelets']
    parent2.dataMatrix['data'] = ind2['data']

    # print(parent1.dataMatrix)

    # return Population.Individual(ind1), Population.Individual(ind2)
    return parent1, parent2


def breedPopulation(matingpool):
    children = []
    length = len(matingpool)
    
    for i in range(0, length):

        if i % 2 != 0:

            child1, child2 = breedIndividual(matingpool[i - 1],matingpool[i])
            
            children.append(child2)
            children.append(child2)

    return children


# mutação

def mutateIndividual(individual, mutationRate):

    # percorre os movelets no individuo
    for swapped in individual.movelets:

        if(random.random() < mutationRate):
            
            swapped.mutate()

            #  zera o score do individuo para recalcular a matriz de distancias
            individual.cleanScore()

    return individual


def mutatePopulation(population, mutationRate):
    
    mutatedPop = []
    
    for individual in population:

        mutatedInd = mutateIndividual(individual=individual, mutationRate=mutationRate)

        mutatedPop.append(mutatedInd)
        
    return mutatedPop

from src import Population

import random

#TODO: revisar
def breedIndividual(parent1, parent2):

    ind1 = []
    ind2 = []

    # print("FATHER ONE")
    # for i in parent1.movelets: 
    #     print(i)

    # print("FATHER TWO")
    # for i in parent2.movelets: 
    #     print(i)

    #  define o ponto de corte
    splitPoint = random.randrange(parent1.size() - 1)
    # splitPoint = int(parent1.size() / 2)

    for i in range(parent1.size()):

        if i < splitPoint:

            ind1.append(parent1.movelets[i])
            ind2.append(parent2.movelets[i])

        else:

            ind1.append(parent2.movelets[i])
            ind2.append(parent1.movelets[i])


    # print("CHILDREN ONE")
    # for i in ind1: 
    #     print(i)

    # print("CHILDREN TWO")
    # for i in ind2: 
    #     print(i)

    return Population.Individual(ind1), Population.Individual(ind2)



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

    return individual


def mutatePopulation(population, mutationRate):
    
    mutatedPop = []
    
    for individual in population:

        mutatedInd = mutateIndividual(individual=individual, mutationRate=mutationRate)

        mutatedPop.append(mutatedInd)
        
    return mutatedPop
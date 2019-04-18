
import random

#TODO: revisar
def crossover(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breed(matingpool):
    children = []
    length = len(matingpool)
    pool = random.sample(matingpool, len(matingpool))
    
    for i in range(0, length):
        child = crossover(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children


# mutação

# TODO: implementar a mutação
def mutation(individual, mutationRate):
    # for swapped in range(len(individual)):
    #     if(random.random() < mutationRate):
    #         swapWith = int(random.random() * len(individual))
            
    #         city1 = individual[swapped]
    #         city2 = individual[swapWith]
            
    #         individual[swapped] = city2
    #         individual[swapWith] = city1
    return individual


def mutate(population, mutationRate):
    
    mutatedPop = []
    
    for ind in range(0, len(population)):

        mutatedInd = mutate(population[ind], mutationRate)

        mutatedPop.append(mutatedInd)
        
    return mutatedPop
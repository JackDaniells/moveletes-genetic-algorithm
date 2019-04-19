
import operator, random

class Fitness:
    def __init__(self, individual):
        self.individual = individual
        self.fitness = 0
        self.rank()
    
    #TODO: implementar o classificador
    def rank(self):

        if self.fitness == 0:

            self.fitness = random.randrange(100)

        return self.fitness
    

def rankPopulation(population):
    
    fitness = []
    
    for ind in population:

        f = Fitness(ind)
        
        fitness.append(f)

    return sorted(fitness, key = operator.attrgetter('fitness'), reverse = True)



def selection(popRanked, eliteSize):

    selectionResults = []

    for i in range(0, eliteSize):

        selectionResults.append(popRanked[i].individual)

    return selectionResults
   
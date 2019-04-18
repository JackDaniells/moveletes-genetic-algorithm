
import operator, random

class Fitness:
    def __init__(self, individual):
        self.individual = individual
        self.fitness= 0.0
    
    #TODO: implementar o classificadors
    def rank(self):

        if self.fitness == 0:

            self.fitness = random.randrange(100)

        return self.fitness
    

def rankRoutes(population):
    
    fitnessResults = {}
    
    for i in range(0,len(population)):

        fitnessResults[i] = Fitness(population[i]).rank()

    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)



def selection(popRanked, eliteSize):

    selectionResults = []
    
    for i in range(0, eliteSize):

        selectionResults.append(popRanked[i])

    return selectionResults
   
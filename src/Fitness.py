
import operator, random, datetime

from src import Classification


class Fitness:
    def __init__(self, individual, trajectories):
        self.individual = individual
        self.trajectories = trajectories
        self.fitness = 0
        self.rank()
    
    def rank(self):


        # print("[" + str(datetime.datetime.now()) + "] " + "Calculating Individual Fitness...")
       
        distanceMatix = Classification.calculateDistanceMatrix(movelets=self.individual.movelets, trajectories=self.trajectories)

        score = Classification.calculateScore(distanceMatix)

        # print("[" + str(datetime.datetime.now()) + "] " + "Done!")
        # usar o dtw pra calcular distancia de cada movelet pra cada trajetoria e depois jogar isso no classificador (Naive Bayes)

        # salvar o dataset e fazer crossover dele tambem na reprodução pra nao precisar calcular tudo de novo

        print(score)

        return score
    

def rankPopulation(population, trajectories):
    
    fitness = []
    
    for ind in population:

        f = Fitness(individual=ind, trajectories=trajectories)
        
        fitness.append(f)

    return sorted(fitness, key = operator.attrgetter('fitness'), reverse = True)



def selection(popRanked, eliteSize):

    selectionResults = []

    for i in range(0, eliteSize):

        selectionResults.append(popRanked[i].individual)

    return selectionResults
   
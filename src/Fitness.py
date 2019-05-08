
import operator, random, datetime, pandas, numpy

from src import Classification


    
def rankIndividual(individual, trajectories):


    # print("[" + str(datetime.datetime.now()) + "] " + "Calculating Individual Fitness...")
    
    distanceMatix = Classification.calculateDistanceMatrix(individual=individual, trajectories=trajectories)

    individual.score = Classification.calculateScore(distanceMatix)

    # print("[" + str(datetime.datetime.now()) + "] " + "Done!")
    # usar o dtw pra calcular distancia de cada movelet pra cada trajetoria e depois jogar isso no classificador (Naive Bayes)

    # salvar o dataset e fazer crossover dele tambem na reprodução pra nao precisar calcular tudo de novo

    print("[" + str(datetime.datetime.now()) + "] " + str(individual.score))

    return individual
    

def rankPopulation(population, trajectories):
    
    fitness = []
    
    for ind in population:

        ftnss = rankIndividual(individual=ind, trajectories=trajectories)
        
        fitness.append(ftnss)

    return sorted(fitness, key = operator.attrgetter('score'), reverse = True)


def selection(popRanked, eliteSize):

    selectionResults = []


    # maxSum = sum(popRanked.score)
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i])

    # for i in range(0, len(popRanked) - eliteSize):

    #     pick = 100 * random.random()
        
    #     for i in range(0, len(popRanked)):
        
    #         if pick >= maxSum:
        
    #             selectionResults.append(popRanked[i])
        
    #             break
    
    return selectionResults



   

import operator, random, datetime, pandas, numpy, gc

from src import Classification



    
def rankIndividual(individual, trainTrajectories, testTrajectories):


    # print("[" + str(datetime.datetime.now()) + "] " + "Calculating Individual Fitness...")

    score = individual.score

    if score == 0:

        # print("[" + str(datetime.datetime.now()) + "] getting distance matrix..")
    
        distanceMatixTrain = Classification.calculateDistanceMatrix(individual=individual, trajectories=trainTrajectories, fileType='train')
        distanceMatixTest = Classification.calculateDistanceMatrix(individual=individual, trajectories=testTrajectories, fileType='test')

        # print(hex(id(distanceMatix)))

        # print("[" + str(datetime.datetime.now()) + "] calcing score...")

        score = Classification.calculateScore(distanceMatixTrain, distanceMatixTest)

        # print("[" + str(datetime.datetime.now()) + "] " + "Done!")

        # salvar o dataset e fazer crossover dele tambem na reprodução pra nao precisar calcular tudo de novo

        del distanceMatixTrain, distanceMatixTest

        gc.collect()

    print("[" + str(datetime.datetime.now()) + "] " + str(score) + ' - ' + str(individual))
    
    return score
    

def rankPopulation(population, trainTrajectories, testTrajectories):
        
    for ind in population:

        ind.score = rankIndividual(individual=ind, trainTrajectories=trainTrajectories, testTrajectories=testTrajectories)
        
        # fitness.append(ind)

        gc.collect()

    # del population

    return sorted(population, key = operator.attrgetter('score'), reverse = True)


def selection(popRanked, eliteSize):

    selectionResults = []

    popConverted = []

    for individual in popRanked:        
        popConverted.append(individual.getValues())

    df = pandas.DataFrame(numpy.array(popConverted), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = df.cum_sum / df.Fitness.sum()


    # elitism
    for i in range(0, eliteSize):
        
        selectionResults.append(popConverted[i][0])

    # roullete whell
    for i in range(0, len(popConverted) - eliteSize):

        pick = random.random()

        for i in range(0, len(popConverted)):

            if pick <= df.iat[i,3]:

                selectionResults.append(popConverted[i][0])
                break


   
    for i in range(0, len(selectionResults)):
        
        # print(selectionResults[i])
        # print(i)
        
        for individual in popRanked:

            if individual.id == selectionResults[i]:

                selectionResults[i] = individual
                break



    # maxSum = sum(popRanked.score)
    
    # for i in range(0, eliteSize):
    #     selectionResults.append(popRanked[i])

    # for i in range(0, len(popRanked) - eliteSize):

    #     pick = 100 * random.random()
        
    #     for i in range(0, len(popRanked)):
        
    #         if pick >= maxSum:
        
    #             selectionResults.append(popRanked[i])
        
    #             break

    del popConverted, popRanked
    
    return selectionResults



   
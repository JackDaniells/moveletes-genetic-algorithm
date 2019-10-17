
import operator, random, datetime, pandas, numpy, gc

from src import Classification



    
def rankIndividual(individual, trajectories, experimental, classificator):

    score = individual.score

    if score == 0:
    
        distanceMatix = Classification.calculateDistanceMatrix(individual=individual, trajectories=trajectories)

        score = Classification.calculateScore(experimental, classificator, distanceMatix)

        del distanceMatix

        gc.collect()

    #  print("[" + str(datetime.datetime.now()) + "] " + str(score) + ' - ' + str(individual))
    
    return score
    

def rankPopulation(population, trajectories, experimental, classificator):
        
    for ind in population:

        ind.score = rankIndividual(individual=ind, trajectories=trajectories, experimental=experimental, classificator=classificator)

        gc.collect()

    return sorted(population, key = operator.attrgetter('score'), reverse = True)


def selection(popRanked, eliteSize, method = 'tournament'):

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


    # another selection
    for i in range(0, len(popConverted) - eliteSize):

        # roullete whell
        if method == 'roullete':
            selectionResults.append(roulleteWhellSelection(popConverted, df))
        
        # tournament
        elif method == 'tournament':
            selectionResults.append(tournamentSelection(popConverted))
           


   
    for i in range(0, len(selectionResults)):
        
        for individual in popRanked:

            if individual.id == selectionResults[i]:

                selectionResults[i] = individual
                break

    del popConverted, popRanked
    
    return selectionResults



def roulleteWhellSelection(pop, df):

    pick = random.random()

    for i in range(0, len(pop)):

        if pick <= df.iat[i,3]:
            return pop[i][0]



def tournamentSelection(pop):

    # Pick individuals for tournament
    fighter_1 = random.randint(0, len(pop) - 1)
    fighter_2 = random.randint(0, len(pop) - 1)
    
    # Get fitness score for each
    fighter_1_fitness = pop[fighter_1][1]
    fighter_2_fitness = pop[fighter_2][1]

    if fighter_1_fitness >= fighter_2_fitness:
        winner = fighter_1
    else:
        winner = fighter_2

    return pop[winner][0]



   
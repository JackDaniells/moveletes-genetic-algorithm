
from src import MatingPool, Fitness

import datetime

import gc

# import tracemalloc


# roda o AG
def run(population, eliteSize, mutationRate, generations, trajectories, notConvergenceLimit, experimental, selectionMethod, classificator):

    gen = population

    # tracemalloc.start()
    
    progress = []

    avgProgress = []

    worstProgress = []

    tempBetterScore = 0

    notConvergenceCount = 0
    
    for i in range(0, generations):

        #  print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i) )

        newGen, betterScore, avgScore, worstScore, bestIndividual = nextGeneration(
            currentGen=gen, 
            eliteSize=eliteSize, 
            mutationRate=mutationRate, 
            trajectories=trajectories,
            experimental=experimental,
            selectionMethod=selectionMethod,
            classificator=classificator
        )

        del gen

        gen = newGen

        # betterScore = 0

        # for i in newGen:
        #     #  print(i)
        #     if i.score > betterScore:
        #         betterScore = i.score

        progress.append(betterScore)

        avgProgress.append(avgScore)

        worstProgress.append(worstScore)

        #  print(betterScore)

        # para o processamento quando nao tem mais convergencia
        if betterScore == tempBetterScore:
            notConvergenceCount += 1
        
        else:
            tempBetterScore = betterScore
            notConvergenceCount = 0

        if notConvergenceCount > 0 and notConvergenceCount % 10 == 0:
            mutationRate = mutationRate * 2
            if mutationRate > 0.5: 
                mutationRate = 0.5
            #  print('---------------------------------')
            #  print('---------------------------------')
            #  print('mutationRate: ' + str(mutationRate))
            #  print('---------------------------------')
            #  print('---------------------------------')

        if (notConvergenceCount == notConvergenceLimit and notConvergenceLimit != 0) or betterScore == 1:
            # #  print('PARADA FORÇADA POR NAO CONVERGENCIA')
            return progress, bestIndividual


        gc.collect()

        
        # snapshot = tracemalloc.take_snapshot()
        # top_stats = snapshot.statistics('lineno')

        # #  print("[ Top 10 ]")
        # for stat in top_stats[:10]:
        #     #  print(stat)

        # #  print("[ Top 10 ]")
        # for stat in top_stats[:10]:
        #     #  print(stat)
    
    return progress, bestIndividual


# crias as novas gerações da população
def nextGeneration(currentGen, eliteSize, mutationRate, trajectories, experimental, selectionMethod, classificator):

    # rankeia os individuos
    #  print("[" + str(datetime.datetime.now()) + "] rankPopulation")
    population = Fitness.rankPopulation(population=currentGen, trajectories=trajectories, experimental=experimental, classificator=classificator)

    bestRanked = population[0].score

    bestIndividual = population[0]

    worstRanked = population[len(population) - 1].score

    avgScore = 0

    for p in population:
        avgScore += p.score

    avgScore = avgScore / len(population)

    # #  print('Fitness.rankPopulation '  + str(len(population)))
    
    # seleciona os melhores para reprodução
    #  print("[" + str(datetime.datetime.now()) + "] selection")
    population = Fitness.selection(popRanked=population, eliteSize=eliteSize, method=selectionMethod)

    # #  print('Fitness.selection '  + str(len(population)))


    # limpa a variavel da memoria        
    # del popRanked


    # faz o crossover entre os individuos
    #  print("[" + str(datetime.datetime.now()) + "] crossover")
    children = MatingPool.breedPopulation(matingpool=population, eliteSize=eliteSize)

    # #  print('MatingPool.breedPopulation '  + str(len(children)))


    # limpa a variavel da memoria
    del population

    # faz a mutação dos indivíduos
    #  print("[" + str(datetime.datetime.now()) + "] mutation")
    children = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate, eliteSize=eliteSize, trajectories=trajectories)

    # #  print('MatingPool.mutatePopulation '  + str(len(children)))

    
    return children, bestRanked, avgScore, worstRanked, bestIndividual
    
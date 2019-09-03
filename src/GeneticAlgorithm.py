
from src import MatingPool, Fitness

import datetime

import gc

# import tracemalloc



# roda o AG
def run(population, eliteSize, mutationRate, generations, trajectories):

    # tracemalloc.start()

    gen = population

<<<<<<< HEAD
=======
    # tracemalloc.start()
    
>>>>>>> af99f2733843a6668dc98c07ded0b92a4aeaf3f3
    progress = []
    
    for i in range(0, generations):

        print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i) )

        gen, betterScore = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)

        # betterScore = 0
        # for i in gen:
        #     if i.score > betterScore:
        #         betterScore = i.score

        progress.append(betterScore)

        print(betterScore)

        
        # snapshot = tracemalloc.take_snapshot()
        # top_stats = snapshot.statistics('lineno')

        # print("[ Top 10 ]")
        # for stat in top_stats[:10]:
        #     print(stat)

        # print("[ Top 10 ]")
        # for stat in top_stats[:10]:
        #     print(stat)
    
    return progress


# crias as novas gerações da população
def nextGeneration(currentGen, eliteSize, mutationRate, trajectories):

    # rankeia os individuos
    print("[" + str(datetime.datetime.now()) + "] rankPopulation")
    popRanked = Fitness.rankPopulation(population=currentGen, trajectories=trajectories)
    
    # seleciona os melhores para reprodução
    print("[" + str(datetime.datetime.now()) + "] selection")
    selectionResults = Fitness.selection(popRanked=popRanked, eliteSize=eliteSize)

    bestRanked = selectionResults[0].score

    # limpa a variavel da memoria        
    del popRanked


    # faz o crossover entre os individuos
    print("[" + str(datetime.datetime.now()) + "] crossover")
    children = MatingPool.breedPopulation(matingpool=selectionResults, eliteSize=eliteSize)

    # limpa a variavel da memoria
    del selectionResults

    # faz a mutação dos indivíduos
    print("[" + str(datetime.datetime.now()) + "] mutation")
    nextGeneration = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate)
    
    return nextGeneration, bestRanked
    
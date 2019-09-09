
from src import MatingPool, Fitness

import datetime

import gc

# import tracemalloc



# roda o AG
def run(population, eliteSize, mutationRate, generations, trajectories):

    gen = population

    # tracemalloc.start()
    
    progress = []
    
    for i in range(0, generations):

        print("[" + str(datetime.datetime.now()) + "] " + "Generation " + str(i) )

        newGen, betterScore = nextGeneration(currentGen=gen, eliteSize=eliteSize, mutationRate=mutationRate, trajectories=trajectories)

        del gen

        gen = newGen

        # betterScore = 0
        # for i in gen:
        #     if i.score > betterScore:
        #         betterScore = i.score

        progress.append(betterScore)

        print(betterScore)

        gc.collect()

        
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
    population = Fitness.rankPopulation(population=currentGen, trajectories=trajectories)
    
    # seleciona os melhores para reprodução
    print("[" + str(datetime.datetime.now()) + "] selection")
    population = Fitness.selection(popRanked=population, eliteSize=eliteSize)

    bestRanked = population[0].score

    # limpa a variavel da memoria        
    # del popRanked


    # faz o crossover entre os individuos
    print("[" + str(datetime.datetime.now()) + "] crossover")
    children = MatingPool.breedPopulation(matingpool=population, eliteSize=eliteSize)

    # limpa a variavel da memoria
    del population

    # faz a mutação dos indivíduos
    print("[" + str(datetime.datetime.now()) + "] mutation")
    children = MatingPool.mutatePopulation(population=children, mutationRate=mutationRate)

    
    return children, bestRanked
    
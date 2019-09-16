
from src import Population, Trajectory, GeneticAlgorithm
import matplotlib.pyplot as plt
import datetime


MOVELET_MIN_SIZE = 4
MOVELET_MAX_SIZE = 5

def run(DATASET_NAME, INDIVIDUAL_SIZE, POPULATION_SIZE, ELITE_SIZE, MUTATION_RATE, GENERATIONS):

    if POPULATION_SIZE <= ELITE_SIZE:
        print ('PARAMETROS INCORRETOS')
        return

    print("[" + str(datetime.datetime.now()) + "] " + "Program started!")


    #le as trajetorias
    print("[" + str(datetime.datetime.now()) + "] " + "Reading files from dataset" + DATASET_NAME  + "...")

    trajectories = Trajectory.readDataset(DATASET_NAME, MOVELET_MAX_SIZE)

    print("[" + str(datetime.datetime.now()) + "] " + "Trajectories found: " + str(len(trajectories)))

    # for t in trajectories:
    #     print(t)


    #cria os individuos
    print("[" + str(datetime.datetime.now()) + "] " + "Creating population...")

    pop = Population.create(trajetories=trajectories, individualSize=INDIVIDUAL_SIZE, populationSize=POPULATION_SIZE, moveletMinSize=MOVELET_MIN_SIZE, moveletMaxSize=MOVELET_MAX_SIZE)

    print("[" + str(datetime.datetime.now()) + "] " + "Population size: " + str(len(pop)))


    #instancia o algoritmo genetico
    print("[" + str(datetime.datetime.now()) + "] " + "Running Genetic Algorithm...")
    print("[" + str(datetime.datetime.now()) + "] " + "Generations: " + str(GENERATIONS))

    # GeneticAlgorithm.run(population=pop, eliteSize=ELITE_SIZE, mutationRate=MUTATION_RATE, generations=GENERATIONS, trajectories=trajectories)

    startTime = datetime.datetime.now()

    progress = GeneticAlgorithm.run(population=pop, eliteSize=ELITE_SIZE, mutationRate=MUTATION_RATE, generations=GENERATIONS, trajectories=trajectories)

    finishTime = datetime.datetime.now()

    diffTime =  finishTime - startTime

    # imprime o progresso 
    plotTitle = DATASET_NAME + '_g' + str(GENERATIONS) + '_p' + str(POPULATION_SIZE) + '_i' + str(INDIVIDUAL_SIZE) + '_e' + str(ELITE_SIZE) + '_t' + str(diffTime)
    plt.plot(progress)
    plt.title(plotTitle)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.show()

    # plt.savefig('results/' + DATASET_NAME + '_' + str(int(finishTime.timestamp())) + '.png')

    print("[" + str(datetime.datetime.now()) + "] " + "Program completed!")

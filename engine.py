
from src import Population, Trajectory, GeneticAlgorithm, Classification
import matplotlib.pyplot as plt
import time, datetime


def run(
    EXPERIMENTAL, 
    DATASET_NAME, 
    CLASSIFICATOR, 
    INDIVIDUAL_SIZE, 
    POPULATION_SIZE, 
    ELITE_SIZE, 
    MUTATION_RATE,
    MUTATION_MULT_FACTOR,
    MUTATION_NOT_CONVERGENCE_LIMIT,
    GENERATIONS, 
    NOT_CONVERGENCE_LIMIT, 
    MOVELET_MIN_SIZE, 
    MOVELET_MAX_SIZE, 
    SELECTION_METHOD
):

    if POPULATION_SIZE <= ELITE_SIZE:
        #  print ('PARAMETROS INCORRETOS')
        return

    #  print("[" + str(datetime.datetime.now()) + "] " + "Program started!")


    #le as trajetorias
    #  print("[" + str(datetime.datetime.now()) + "] " + "Reading files from dataset" + DATASET_NAME  + "...")

    trainTrajectories = Trajectory.readDataset(EXPERIMENTAL, 'train', DATASET_NAME, MOVELET_MAX_SIZE)

    #  print("[" + str(datetime.datetime.now()) + "] " + "Trajectories found: " + str(len(trainTrajectories)))

    # for t in trajectories:
    #     #  print(t)


    #cria os individuos
    #  print("[" + str(datetime.datetime.now()) + "] " + "Creating population...")

    #  print(datetime.datetime.now())
    pop = Population.create(
        trajetories=trainTrajectories, 
        individualSize=INDIVIDUAL_SIZE, 
        populationSize=POPULATION_SIZE, 
        moveletMinSize=MOVELET_MIN_SIZE, 
        moveletMaxSize=MOVELET_MAX_SIZE
    )
    #  print(datetime.datetime.now())

    #  print("[" + str(datetime.datetime.now()) + "] " + "Population size: " + str(len(pop)))


    #instancia o algoritmo genetico
    #  print("[" + str(datetime.datetime.now()) + "] " + "Running Genetic Algorithm...")
    #  print("[" + str(datetime.datetime.now()) + "] " + "Generations: " + str(GENERATIONS))

    startTime = int(time.time())

    progress, bestIndividual = GeneticAlgorithm.run(
        population=pop, 
        eliteSize=ELITE_SIZE, 
        mutationRate=MUTATION_RATE,
        mutationMultFactor=MUTATION_MULT_FACTOR,
        mutationNotConvergenceLimit=MUTATION_NOT_CONVERGENCE_LIMIT,
        generations=GENERATIONS, 
        trajectories=trainTrajectories, 
        notConvergenceLimit=NOT_CONVERGENCE_LIMIT,
        experimental=EXPERIMENTAL,
        selectionMethod=SELECTION_METHOD,
        classificator=CLASSIFICATOR
    )

    finishTime = int(time.time())

    diffTime =  finishTime - startTime

    # imprime o progresso 
    plotTitle = DATASET_NAME + '_g' + str(GENERATIONS) + '_p' + str(POPULATION_SIZE) + '_i' + str(INDIVIDUAL_SIZE) + '_e' + str(ELITE_SIZE) + '_m' + str(MUTATION_RATE) + '_t' + str(datetime.timedelta(seconds=diffTime))
    plt.plot(progress)
    plt.title(plotTitle)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    # plt.show()
    plt.savefig('results/' + DATASET_NAME + '_' + str(finishTime) + '.png')

    plt.clf()

    if EXPERIMENTAL != 'E1':

        testTrajectories = Trajectory.readDataset(EXPERIMENTAL, 'test', DATASET_NAME, MOVELET_MAX_SIZE)

        distanceMatixTrain = Classification.calculateDistanceMatrix(individual=bestIndividual, trajectories=trainTrajectories, fileType='train')
        distanceMatixTest = Classification.calculateDistanceMatrix(individual=bestIndividual, trajectories=testTrajectories, fileType='test')

        score = Classification.calculateScore(EXPERIMENTAL, CLASSIFICATOR, distanceMatixTrain, distanceMatixTest)

    else:

        score = bestIndividual.score

    #  print("Best: " + str(score) + " - Time: " + str(diffTime))
    #  print("[" + str(datetime.datetime.now()) + "] " + "Program completed!")

    return score, diffTime

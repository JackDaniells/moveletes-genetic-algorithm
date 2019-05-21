# from scipy.spatial import distance
import timeit, numpy, time 

from fastdtw import fastdtw

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

DECIMAL_FIELDS = 4

    

def calculateDistanceMatrix(individual, trajectories):


    dataMatrix = {
        'data': [],
        'classes': []
    }

    dataMatrixCol = []

    # itera o individuo
    for i in range(0, len(trajectories)):

        trajectory = trajectories[i]

        t1 = trajectory.getPoints()

    
        dataMatrixCol = []
    

        # itera as trajetorias
        for j in range(0, len(individual.movelets)):

            movelet = individual.movelets[j]

            distance = 0

            # verifica se a distancia ja esta calculada
            if len(movelet.distances) == len(trajectories): 

                distance = movelet.distances[i]

            else:

                t2 = movelet.getPoints()

                
                # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0
                if movelet.trajectory.fileName != trajectory.fileName:
                    start = timeit.default_timer()

                    distance, path = fastdtw(t1, t2, dist=euclidean)

                    end = timeit.default_timer()

                # d = d[dtw] / |movelet|
                # distance = round(float(distance / len(t1)), 2)

                distance = round(float(distance), DECIMAL_FIELDS)

                movelet.distances.append(distance)

            dataMatrixCol.append(distance)

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(trajectory.group)

    # print(dataMatrix)

    return dataMatrix

def calculateScore(dataMatrix):
    
    CROSS_VALIDATION_FOLDS = 2

    naiveBayes = GaussianNB()
    
    # cross validation
    gs = GridSearchCV(naiveBayes, cv=CROSS_VALIDATION_FOLDS, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 

    gs.fit(dataMatrix['data'], dataMatrix['classes'])

    # naiveBayes.fit(dataMatrix['data'], dataMatrix['classes'])
    # print(naiveBayes.score(dataMatrix['data'], dataMatrix['classes']))
    # print(gs.cv_results_)

    result = gs.cv_results_['mean_test_score'][0]

    return round(result, DECIMAL_FIELDS)



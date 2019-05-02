# from scipy.spatial import distance
import timeit, numpy, time 

from fastdtw import fastdtw

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

from sklearn.datasets import load_iris

    

# calcula a distancia com fastdtw
def calculateDistanceMatrix(movelets, trajectories):

    dataMatrix = {
        'data': [],
        'classes': []
    }

    dataMatrixCol = []

    # itera o individuo
    for i in range(0, len(movelets)):

        movelet = movelets[i]

        t1 = movelet.getPoints()

        dataMatrixCol = []
    

        # itera as trajetorias
        for j in range(0, len(trajectories)):

            trajectory = trajectories[j]

            t2 = trajectory.getPoints()

            distance = 0
            
            # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0
            if movelet.trajectory.fileName != trajectory.fileName:
                # start = timeit.default_timer()

                distance, path = fastdtw(t1, t2, dist=euclidean)

                # end = timeit.default_timer()

            # d = d[dtw] / |movelet|
            distance = round(float(distance / len(t1)), 2)

            dataMatrixCol.append(distance)

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(movelet.trajectory.group)

    # print(dataMatrix)

    return dataMatrix

def calculateScore(dataMatrix):
    
    naiveBayes = GaussianNB()
    
    # cross validation
    gs = GridSearchCV(naiveBayes, cv=2, param_grid={}, return_train_score=True, n_jobs=-1, iid=True) 

    gs.fit(dataMatrix['data'], dataMatrix['classes'])

    # naiveBayes.fit(dataMatrix['data'], dataMatrix['classes'])
    # print(naiveBayes.score(dataMatrix['data'], dataMatrix['classes']))
    # print(gs.cv_results_)

    return gs.cv_results_['mean_test_score'][0]



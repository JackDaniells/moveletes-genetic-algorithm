# from scipy.spatial import distance
import timeit, numpy, time, datetime

# from sklearn.svm import SVR

import multiprocessing

# import pyopencl as cl

from sklearn.naive_bayes import GaussianNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn import preprocessing


DECIMAL_FIELDS = 4

USE_CROSS_VALIDATION = False

# ----------------------------------------------------------
def calculateMovetelDistance(movelet, trajectory, trajectoryPoints, fileType):

    # #  print('[calculateMovetelDistance]')
    # movelet = individual.movelets[moveletPosition]

    distance = 0

    # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0            
    if trajectory.fileName == movelet.trajectory.fileName and fileType == 'train':
        distance = 0

    # verifica se a distancia ja esta calculada
    elif trajectory.fileName in movelet.distances and fileType == 'train':

        # #  print('array de distancias calculada')

        distance = movelet.distances[trajectory.fileName]

    else:

        # #  print('array de distancias nao calculada')

        moveletPoints = movelet.getPoints()

        distance = 0

        moveletsIteractions = len(moveletPoints)

        trajectoryIteractions = len(trajectoryPoints) - len(moveletPoints) + 1

        for t in range(0, trajectoryIteractions):

            distanceCalculated = 0

            for m in range(0, moveletsIteractions):

                p = t + m

                distanceCalculated += euclidean(trajectoryPoints[p], moveletPoints[m])
                
            # divide a distancia pela qtde de movelets
            if distanceCalculated > 0:
                distanceCalculated = distanceCalculated / len(moveletPoints)

            # se a distancia calculada for menor que zero ou for a primeira iteração 
            if distanceCalculated < distance or t == 0:
                distance = distanceCalculated

        
    if fileType == 'train':
        movelet.distances[trajectory.fileName] = distance
            
    return distance


# ----------------------------------------------------------
def calculateDistanceMatrix(individual, trajectories, fileType = 'train'):

    # #  print("[" + str(datetime.datetime.now()) + "] " + "calculateDistanceMatrix start")

    dataMatrix = {
        'data': [],
        'classes': []
    }  


    # itera as trajetorias
    for i in range(0, len(trajectories)):

        trajectory = trajectories[i]

        tp = trajectory.getPoints()

        dataMatrixRow = [calculateMovetelDistance(movelet, trajectory, tp, fileType) for movelet in individual.movelets]  

        dataMatrixRow.append(trajectory.duration)
        dataMatrixRow.append(trajectory.distance)
        dataMatrixRow.append(trajectory.avgSpeed)

        dataMatrix['data'].append(dataMatrixRow)
        dataMatrix['classes'].append(trajectory.group)

    return dataMatrix


# ----------------------------------------------------------
def calculateScore(experimental, method, train, test = {}):

    if method == 'Bayes':
        classifier = GaussianNB(priors=None, var_smoothing=1e-09)
    elif method == 'SVM':
        classifier = SVC(gamma='auto')
    elif method == 'C45':
        classifier = DecisionTreeClassifier(min_samples_split=10, criterion='entropy', max_depth=5)

    

    # holdout
    if experimental != 'E1':

        if len(test) != 0:
            return round(holdoutClassification(classifier, train, test), DECIMAL_FIELDS)
        else:
            return round(holdoutClassification(classifier, train, train), DECIMAL_FIELDS)

    # cross validation
    else:
        return round(crossValidationClassification(classifier, train), DECIMAL_FIELDS)

        


     

def holdoutClassification(classifier, trainMatrix, testMatrix):

    # #  print('holdoutClassification')

    x_train = trainMatrix['data']
    y_train = trainMatrix['classes']

    x_test = testMatrix['data']
    y_test = testMatrix['classes']

    classifier.fit(x_train, y_train)
    return classifier.score(x_test, y_test)
    

def crossValidationClassification(classifier, matrix, folds = 2):

    # #  print('crossValidationClassification')

    x_train = matrix['data']
    y_train = matrix['classes']

    gs = GridSearchCV(classifier, cv=folds, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 

    gs.fit(x_train, y_train)

    return gs.cv_results_['mean_test_score'][0]


def saveInCSV(x, y): 
    
    dataToCSV = []
    
    for i in range(0, len(x)):
        
        x_copy = numpy.array(x[i].copy())

        x_copy = numpy.append(x_copy, y[i])


        dataToCSV.append(x_copy)
        # numpy.append(dataToCSV[i], y[i])
    # numpy.append(a, dataMatrix['classes'])

    a = numpy.asarray(dataToCSV)

    numpy.savetxt("csv/"+ str(timeit.default_timer()) +".csv", a, delimiter=",", fmt='%s')



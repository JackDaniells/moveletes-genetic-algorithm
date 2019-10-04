# from scipy.spatial import distance
import timeit, numpy, time, datetime

from sklearn.svm import SVR

import multiprocessing, json

from datetime import datetime
import time

# import pyopencl as cl

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

from sklearn.metrics import classification_report

from sklearn import preprocessing

# from lib import levenshtein


DECIMAL_FIELDS = 8


# 1 = holdout
# 2 = cross-validation
CLASSIFICATION_METHOD = 1

def getDistance(first, second, attribute):

    dst = 0

    if attribute['type'] == 'String':
        second = str(second)
        first = str(first)
    elif attribute['type'] == 'Number':
        second = float(second)
        first = float(first)


    # if attribute['distance'] == 'levenshtein':
    #     dst = levenshtein.distance(str(first), str(second), True)

    if attribute['distance'] == 'weekday':
        weekdays =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        tp = 1 if first in weekdays else 0       
        mp = 1 if second in weekdays else 0
        dst = 0 if tp == mp else 1

    elif attribute['distance'] == 'binary':
        dst = 0 if first == second else 1

    elif attribute['distance'] == 'difference':
        first = first if int(first) != -999 else 5
        second = second if int(second) != -999 else 5
        dst = abs(first - second)

    return dst


# ----------------------------------------------------------
def calculateMovetelDistance(movelet, trajectory):

    # print('[calculateMovetelDistance]')
    # movelet = individual.movelets[moveletPosition]

    trajectoryPoints = trajectory.getPoints()

    distance = 0

    # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0            
    if trajectory.fileName == movelet.trajectory.fileName:
        distance = 0

    # verifica se a distancia ja esta calculada
    elif trajectory.fileName in movelet.distances:

        # print('array de distancias calculada')

        distance = movelet.distances[trajectory.fileName]

    else:

        # print('array de distancias nao calculada')

        moveletPoints = movelet.getPoints()

        distance = 0

        moveletsIteractions = len(moveletPoints)

        trajectoryIteractions = len(trajectoryPoints) - len(moveletPoints) + 1

        for t in range(0, trajectoryIteractions):

            distanceCalculated = 0


            # calcula a distancia do movelet para a trajetoria
            for m in range(0, moveletsIteractions):

                p = t + m

                # trajetorias multiaspecto
                if trajectory.datasetName == 'Foursquare':
                    
                    with open('./datasets/Foursquare/description.json', 'r') as f:
                        description = json.load(f)

                    # calcula a di
                    # stancia dos pontos
                    movelet.attributeDistances['point'] = euclidean(trajectoryPoints[p].getPosition(), moveletPoints[m].getPosition())

                    # calcula a distancia do tempo
                    a = datetime.strptime(trajectoryPoints[p].time, '%Y-%m-%d %H:%M:%S')
                    b = datetime.strptime(moveletPoints[m].time, '%Y-%m-%d %H:%M:%S')

                    d1_ts = time.mktime(a.timetuple())
                    d2_ts = time.mktime(b.timetuple())

                    movelet.attributeDistances['time'] = abs((d2_ts-d1_ts) / 60)

                    for a in description['attributes']:

                        tValue = trajectoryPoints[p].attributes[a['value']]
                        mValue = moveletPoints[m].attributes[a['value']]

                        # retorna a distancia entre os atributos
                        movelet.attributeDistances[a['value']] = getDistance(first=tValue, second=mValue, attribute=a)

                    # distanceCalculated += (attDist + xyDistance) /  len(description['attributes']) + 1

                # trajetorias normais
                else:

                    distanceCalculated += euclidean(trajectoryPoints[p], moveletPoints[m])
                
            # divide a distancia pela qtde de movelets
            if distanceCalculated > 0:
                distanceCalculated = distanceCalculated / len(moveletPoints)

            # print(distanceCalculated) 

            # se a distancia calculada for menor que zero ou for a primeira iteração 
            if distanceCalculated < distance or t == 0:
                distance = distanceCalculated

        
    movelet.distances[trajectory.fileName] = distance
            
    return distance


# ----------------------------------------------------------
def calculateDistanceMatrix(individual, trajectories):

    # print("[" + str(datetime.datetime.now()) + "] " + "calculateDistanceMatrix start")

    dataMatrix = {
        'data': [],
        'classes': []
    }

    # itera as trajetorias
    for i in range(0, len(trajectories)):

        trajectory = trajectories[i]

        dataMatrixCol = [calculateMovetelDistance(movelet, trajectory) for movelet in individual.movelets]  

        # print('start pool')
        # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        # dataMatrixCol = [pool.apply(calculateMovetelDistance, args=(movelet, tp)) for movelet in individual.movelets]
        # print('end pool')
        
        # pool.close()

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(trajectory.group)
                    
    # print("[" + str(datetime.datetime.now()) + "] " + "calculateDistanceMatrix end")

    return dataMatrix


# ----------------------------------------------------------
def calculateScore(dataMatrix):
        
    # print("[" + str(datetime.datetime.now()) + "] " + "classification started")

    naiveBayes = GaussianNB(priors=None, var_smoothing=1e-09)
    
    # normaliza e padroniza dos dados

    # x_data = dataMatrix['data']

    # x_data = preprocessing.KBinsDiscretizer(n_bins=50, encode='ordinal', strategy='uniform').fit(dataMatrix['data'])

    # x_data = x_data.transform(dataMatrix['data'])

    x_data = preprocessing.normalize(dataMatrix['data'])

    y_data = dataMatrix['classes']

    # salva o csv dos arquivos
    # saveInCSV(x_data, y_data)

    result = 0


    if CLASSIFICATION_METHOD == 1:


        x_train, x_test, y_train, y_test = train_test_split(
            x_data,  
            y_data, 
            test_size=0.4, 
            train_size=0.6, 
            random_state=None,
            shuffle=True
        )

        naiveBayes.fit(x_train, y_train)

        # saveInCSV(x_train, y_train)

        # saveInCSV(x_test, y_test)

        result = naiveBayes.score(x_test, y_test)

        del naiveBayes, x_data, y_data, x_train, x_test, y_train, y_test



    elif CLASSIFICATION_METHOD == 2:

    # cross validation
        gs = GridSearchCV(naiveBayes, cv=CROSS_VALIDATION_FOLDS, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 


        gs.fit(x_data, y_data)

        result = gs.cv_results_['mean_test_score'][0]

        del gs
        

    # print(result)

    # print("[" + str(datetime.datetime.now()) + "] " + "classification end")

    return round(result, DECIMAL_FIELDS)    


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



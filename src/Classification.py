# from scipy.spatial import distance
import timeit, numpy, time 

from sklearn.svm import SVR


from sklearn.naive_bayes import GaussianNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

from sklearn.metrics import classification_report

from sklearn import preprocessing


DECIMAL_FIELDS = 5

    

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
                # if movelet.trajectory.fileName != trajectory.fileName:

                moveletsIteractions =  len(t2) - 1

                trajectoryIteractions = len(t1) - moveletsIteractions

                for t in range(0, trajectoryIteractions):

                    distanceCalculated = 0

                    for m in range(0, moveletsIteractions):

                        p = t + m

                        distanceCalculated += euclidean(t1[p], t2[m])
                        
                
                    if distanceCalculated > 0:
                        distanceCalculated = distanceCalculated / len(t2)

                    # se a distancia calculada for menor que zero ou for a primeira iteração 
                    if distanceCalculated > distance or t == 0:
                        distance = distanceCalculated

                # d = d[dtw] / |movelet|
                # distance = round(float(distance / len(t1)), 2)

                # distance = round(distance, DECIMAL_FIELDS)

                movelet.distances.append(distance)

            dataMatrixCol.append(distance)

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(trajectory.group)

    # print(dataMatrix)

    return dataMatrix





def calculateScore(dataMatrix):
    
    CROSS_VALIDATION_FOLDS = 2

    naiveBayes = GaussianNB()
    
    # print(dataMatrix)

    # salva o csv dos arquivos

    # X_train, X_test, y_train, y_test = train_test_split(
    # dataMatrix['data'],  dataMatrix['classes'], test_size=0.4, random_state=0)


    # normaliza e padroniza dos dados

    x_data = preprocessing.normalize(dataMatrix['data'])

    # x_data = preprocessing.KBinsDiscretizer(n_bins=50, encode='ordinal', strategy='uniform').fit(dataMatrix['data'])

    # x_data = x_data.transform(dataMatrix['data'])

    y_data = dataMatrix['classes']

    # saveInCSV(x_data, y_data)


    # cross validation
    gs = GridSearchCV(naiveBayes, cv=CROSS_VALIDATION_FOLDS, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 

    # gs.fit(X_train, y_train)

    # print(gs.score(X_test, y_test))

    gs.fit(x_data, y_data)

    result = gs.cv_results_['mean_test_score'][0]

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

    numpy.savetxt(""+ str(timeit.default_timer()) +".csv", a, delimiter=",", fmt='%s')



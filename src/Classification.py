# from scipy.spatial import distance
import timeit, numpy, time 

from sklearn.svm import SVR


from sklearn.naive_bayes import GaussianNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

from sklearn.metrics import classification_report

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
                if movelet.trajectory.fileName != trajectory.fileName:

                    start = timeit.default_timer()

                    moveletsIteractions =  len(t2) - 1

                    trajectoryIteractions = len(t1) - moveletsIteractions

                    for t in range(0, trajectoryIteractions):

                        distanceCalculated = 0

                        for m in range(0, moveletsIteractions):

                            p = t + m

                            distanceCalculated += euclidean(t1[p], t2[m])
                    
                        distanceCalculated = distanceCalculated / len(t2)

                        if distanceCalculated < distance or distance == 0:
                            distance = distanceCalculated

                    end = timeit.default_timer()

                # d = d[dtw] / |movelet|
                # distance = round(float(distance / len(t1)), 2)

                distance = round(distance, DECIMAL_FIELDS)

                movelet.distances.append(distance)

            dataMatrixCol.append(distance)

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(trajectory.group)

    # print(dataMatrix)

    return dataMatrix

def calculateScore(dataMatrix):
    
    CROSS_VALIDATION_FOLDS = 10

    naiveBayes = GaussianNB()
    
    # print(dataMatrix)

    # salva o csv dos arquivos
    # dataToCSV = []
    
    # for i in range(0, len(dataMatrix['data'])):
        
    #     dataToCSV.append(dataMatrix['data'][i].copy())

    #     dataToCSV[i].append(dataMatrix['classes'][i])
    # # numpy.append(a, dataMatrix['classes'])

    # a = numpy.asarray(dataToCSV)

    # numpy.savetxt("run/"+ str(timeit.default_timer()) +".csv", a, delimiter=",", fmt='%s')




    X_train, X_test, y_train, y_test = train_test_split(
    dataMatrix['data'],  dataMatrix['classes'], test_size=0.3, random_state=0)




    # cross validation
    gs = GridSearchCV(naiveBayes, cv=CROSS_VALIDATION_FOLDS, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 

    gs.fit(dataMatrix['data'], dataMatrix['classes'])

    # gs.fit(X_train, y_train)

    # print("Best parameters set found on development set:")
    # print()
    # print(gs.best_params_)
    # print()
    # print("Grid scores on development set:")
    # print()
    # means = gs.cv_results_['mean_test_score']
    # stds = gs.cv_results_['std_test_score']
    # for mean, std, params in zip(means, stds, gs.cv_results_['params']):
    #     print("%0.3f (+/-%0.03f) for %r"
    #           % (mean, std * 2, params))
    # print()

    # print("Detailed classification report:")
    # print()
    # print("The model is trained on the full development set.")
    # print("The scores are computed on the full evaluation set.")
    # print()
    # y_true, y_pred = y_test, gs.predict(X_test)
    # print(classification_report(y_true, y_pred))
    # print()





    # naiveBayes.fit(dataMatrix['data'], dataMatrix['classes'])
    # print(naiveBayes.score(dataMatrix['data'], dataMatrix['classes']))
    # print(gs.cv_results_)


    result = gs.cv_results_['mean_test_score'][0]

    return round(result, DECIMAL_FIELDS)    



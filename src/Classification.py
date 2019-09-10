# from scipy.spatial import distance
import timeit, numpy, time, datetime

from sklearn.svm import SVR

# import pyopencl as cl

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from scipy.spatial.distance import euclidean
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

from sklearn.metrics import classification_report

from sklearn import preprocessing


DECIMAL_FIELDS = 8

    

def calculateDistanceMatrix(individual, trajectories):

    # print("[" + str(datetime.datetime.now()) + "] " + "calculateDistanceMatrix start")


    dataMatrix = {
        'data': [],
        'classes': []
    }

    dataMatrixCol = []

    # print(hex(id(dataMatrix)))


    # itera as trajetorias
    for i in range(0, len(trajectories)):

        trajectory = trajectories[i]

        tp = trajectory.getPoints()

        dataMatrixCol = []    

        # #this line would create a context
        # cntxt = cl.create_some_context()
        # #now create a command queue in the context
        # queue = cl.CommandQueue(cntxt)
        
        # itera o individuo
        for j in range(0, len(individual.movelets)):

            movelet = individual.movelets[j]

            distance = 0

            # print(movelet.distances)

            # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0            
            if trajectory.fileName == movelet.trajectory.fileName:
                distance = 0

            # verifica se a distancia ja esta calculada
            elif len(movelet.distances) == len(trajectories):

                # print('array de distancias calculada')

                distance = movelet.distances[i]

            else:

                # print('array de distancias nao calculada')

                # movelet.distances = []

                mp = movelet.getPoints()

                # create the buffers to hold the values of the input
                # mp_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR,hostbuf=mp)
                # tp_buf = cl.Buffer(cntxt, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR,hostbuf=tp)

                # dist_buf = cl.Buffer(cntxt, cl.mem_flags.WRITE_ONLY, distance.nbytes)

                # code = """

                #     #include <math.h>

                #     __kernel void calc_distance(__global int* moveletPoints, __global int* trajectoryPoints,__global int distance) 
                #     {

                #         moveletsIteractions = sizeof(moveletPoints)


                #         trajectoryIteractions = sizeof(trajectoryPoints) - sizeof(moveletPoints) + 1

                #         for (t = 0; t < sizeof(trajectoryIteractions); t++) {

                #             int distanceCalculated = 0

                #             for (int m = 0; m < sizeof(moveletsIteractions); m++) {

                #                 int p = t + m

                #                 distanceCalculated += sqrt(pow((trajectoryPoints[p][0] - moveletPoints[m][0]), 2) + pow((trajectoryPoints[p][1] - moveletPoints[m][1]), 2))

                #             }
                                
                #             if (distanceCalculated > 0)
                #                 distanceCalculated = distanceCalculated / sizeof(moveletPoints)

                #             if (distanceCalculated < distance || t == 0)
                #                 distance = distanceCalculated
                            
                            

                #         }
        
                #     }
                # """

                # # build the Kernel
                # bld = cl.Program(cntxt, code).build()
                # # Kernel is now launched
                # launch = bld.calc_distance(queue, mp_buf.shape, mp_buf,tp_buf,dist_buf)
                # # wait till the process completes
                # launch.wait()

                # cl.enqueue_read_buffer(queue, dist_buf, distance).wait()

                # print(distance)

                
                distance = calculateMovetelDistance(moveletPoints=mp, trajectoryPoints=tp)

                movelet.distances.append(distance)

            dataMatrixCol.append(distance)

        dataMatrix['data'].append(dataMatrixCol)
        dataMatrix['classes'].append(trajectory.group)

        del dataMatrixCol

    # print(dataMatrix)

    dataReturn = dataMatrix.copy()

    del dataMatrix

    # print("[" + str(datetime.datetime.now()) + "] " + "calculateDistanceMatrix end")

    return dataReturn



def calculateMovetelDistance(moveletPoints, trajectoryPoints):

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
        
        
    return distance



def calculateScore(dataMatrix):
        
    # print("[" + str(datetime.datetime.now()) + "] " + "classification started")

    naiveBayes = GaussianNB(priors=None, var_smoothing=1e-09)
    
    # normaliza e padroniza dos dados

    x_data = preprocessing.normalize(dataMatrix['data'])

    # x_data = dataMatrix['data']

    # x_data = preprocessing.KBinsDiscretizer(n_bins=50, encode='ordinal', strategy='uniform').fit(dataMatrix['data'])

    # x_data = x_data.transform(dataMatrix['data'])

    y_data = dataMatrix['classes']

    # salva o csv dos arquivos
    # saveInCSV(x_data, y_data)

    # cross validation
    # gs = GridSearchCV(naiveBayes, cv=CROSS_VALIDATION_FOLDS, param_grid={}, return_train_score=False, n_jobs=-1, iid=True) 


    # gs.fit(x_data, y_data)

    # result = gs.cv_results_['mean_test_score'][0]

    # del gs

    # print(dataMatrix['data'][0])

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



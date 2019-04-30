# from scipy.spatial import distance
import timeit
from fastdtw import fastdtw
    

def calculateDistanceMatrix(movelets, trajectories):

    dataMatrix = []
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


            # start = timeit.default_timer()

            distance = 0
            
            # só calcula se o movelet nao for da trajetoria em questao, senao distancia = 0
            # if movelet.trajectory.fileName != trajectory.fileName
            
            distance, path = fastdtw(t1, t2, dist=None)

            distance = round(float(distance), 2)
            
            # end = timeit.default_timer()

            dataMatrixCol.append(distance)

        dataMatrix.append(dataMatrixCol)

    print(dataMatrix)

    

    return dataMatrix
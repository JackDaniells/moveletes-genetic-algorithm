
import random

# classe movelet
class Movelet:

    def __init__(self, trajectory, start, size):
        self.trajectory = trajectory
        self.start = start
        self.size = size 

    def mutate(self): 
        # pode mutar o tamanho do movelet e o ponto de inicio
        mutateOptions = [
            'size',
            'start'
        ]

        mutationType = mutateOptions[random.randrange(len(mutateOptions))]

        if mutationType == 'size':

            self.size = random.randrange(2, t.size() - self.start)

        elif mutationType == 'start':

            self.start = random.randrange(t.size() - self.size)
    
    def __repr__(self):
        return "(" + str(self.trajectory.fileName) + ":\t | Start:" + str(self.start) + ", Length:" + str(self.size) + ")"


# classe individuo
class Individual:

    def __init__(self, movelets):

        self.movelets = movelets

    def size(self):

        return len(self.movelets)


def create(trajetories, size, popSize):



    population = []

    #  cria os individuos
    for q in range(0, popSize):

        movelets = []

        # cria os movelets
        for s in range(0, size):

            # pega uma trajetoria aleatoriamente
            t = trajetories[random.randrange(len(trajetories))]

            # define o ponto de inicio aleatoriamente
            start = random.randrange(t.size() - 2)

            # define o tamanho do movelet aleatoriamente
            s = random.randrange(2, t.size() - start)

            # cria o movelet
            movelet = Movelet(trajectory=t, start=start, size=s)

            movelets.append(movelet)


        ind = Individual(movelets=movelets)
        
        population.append(ind)
        
    return population


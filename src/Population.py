
import random, uuid

# classe movelet
class Movelet:

    def __init__(self, trajectory, start, size):
        self.trajectory = trajectory
        self.start = start
        self.size = size
        # self.distances = []

    def getPoints(self): 

        sObject = slice(self.start, self.start + self.size)

        points = self.trajectory.points[sObject]

        ret = []

        for p in points:
            ret.append(p.getPosition())

        return ret

    def mutate(self): 
        # pode mutar o tamanho do movelet e o ponto de inicio
        mutateOptions = [
            'size',
            'start'
        ]

        mutationType = mutateOptions[random.randrange(len(mutateOptions))]

        if mutationType == 'size':

            if self.trajectory.size() - self.start > 2:
            
                self.size = random.randrange(2, self.trajectory.size() - self.start)


        elif mutationType == 'start':

            if self.trajectory.size() - self.size > 0:

                self.start = random.randrange(self.trajectory.size() - self.size)
            
    
    def __repr__(self):
        return "(" + str(self.trajectory.fileName) + ":\t | Start:" + str(self.start) + ", Length:" + str(self.size) + ")"


# classe individuo
class Individual:

    def __init__(self, movelets):

        self.id = uuid.uuid4()

        self.movelets = movelets
        
        self.cleanScore()

    def size(self):

        return len(self.movelets)

    def getValues(self):
        
        return [self.id, self.score]

    def cleanScore(self):
       
        self.score = 0

        self.dataMatrix = {
            'data': [],
            'classes': []
        }


def create(trajetories, individualSize, populationSize):

    population = []

    #  cria os individuos
    for q in range(0, populationSize):

        movelets = []

        # cria os movelets
        for s in range(0, individualSize):

            # pega uma trajetoria aleatoriamente
            t = trajetories[random.randrange(len(trajetories))]

            # print(t.size())
            # define o ponto de inicio aleatoriamente
            start = 0
            if t.size() > 2:
                start = random.randrange(t.size() - 2)

            # define o tamanho do movelet aleatoriamente
            s = 2
            if  (t.size() - start) > 2:
                s = random.randrange(2, t.size() - start)

            # cria o movelet
            movelet = Movelet(trajectory=t, start=start, size=s)

            movelets.append(movelet)


        ind = Individual(movelets=movelets)
        
        population.append(ind)
        
    return population


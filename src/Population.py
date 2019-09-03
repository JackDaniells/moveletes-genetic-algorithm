
import random, uuid


# classe movelet
class Movelet:

    def __init__(self, trajectory, start, size, minSize, maxSize):
        self.trajectory = trajectory
        self.start = start
        self.size = size
        self.distances = []
        self.minSize = minSize
        self.maxSize = maxSize

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

        # limpa o array de distancias
        self.distances = []


        mutationType = mutateOptions[random.randrange(len(mutateOptions))]

        if mutationType == 'size':

            if self.trajectory.size() - self.start > self.minSize:
            
                self.size = random.randrange(self.minSize, self.trajectory.size() - self.start)

            if self.maxSize != 0 and self.size > self.maxSize:
                self.size = self.maxSize


        elif mutationType == 'start':

            if self.trajectory.size() - self.size > 0:

                self.start = random.randrange(self.trajectory.size() - self.size)
    
    def __repr__(self):
        return "(" + str(self.trajectory.fileName) + ":\t | Start:" + str(self.start) + ", Length:" + str(self.size) + ")"


# classe individuo
class Individual:

    def __init__(self, movelets, score):

        self.id = uuid.uuid4()

        self.movelets = movelets
        
        self.score = score


    def size(self):

        return len(self.movelets)


    def getValues(self):
        
        return [self.id, self.score]


    def cleanScore(self):
       
        self.score = 0

        

def create(trajetories, individualSize, populationSize, moveletMaxSize, moveletMinSize):

    population = []

    #  cria os individuos
    for q in range(0, populationSize):

        movelets = []

        # cria os movelets
        for s in range(0, individualSize):

            # pega uma trajetoria aleatoriamente
            t = trajetories[random.randrange(0, len(trajetories))]
            
            # t = trajetories[s % len(trajetories)]

            # print(t.size())
            # define o ponto de inicio aleatoriamente
            start = 0
            if t.size() > moveletMinSize:
                start = random.randrange(0, t.size() - moveletMinSize)

            # define o tamanho do movelet aleatoriamente
            s = moveletMinSize
            if  (t.size() - start) > moveletMinSize:
                s = random.randrange(moveletMinSize, t.size() - start)

            if s > moveletMaxSize:
                s = moveletMaxSize 

            # cria o movelet
            movelet = Movelet(trajectory=t,start=start, size=s, maxSize=moveletMaxSize, minSize=moveletMinSize)

           
            # print(movelet)

            movelets.append(movelet)

        ind = Individual(movelets=movelets, score=0)

        # print('============================================')
        
        population.append(ind)
        
    return population


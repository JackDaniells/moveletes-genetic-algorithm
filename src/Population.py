
import random

class Movelet:

    def __init__(self, trajectory, start, size):
        self.trajectory = trajectory
        self.start = start
        self.size = size 
    
    def __repr__(self):
        return "(" + str(self.trajectory.dataset) + " - " + str(self.trajectory.group) + " | Start:" + str(self.start) + ", Length:" + str(self.size) + ")"



class Individual:

    def __init__(self, movelets, size):
        self.movelets = movelets
        self.size = size


def create(trajetories, size, qty):

    population = []

    #  cria os individuos
    for q in range(qty):

        movelets = []

        # cria os movelets
        for s in range(size):

            t = trajetories[random.randrange(len(trajetories))]

            start = random.randrange(t.size() - 1)

            size = random.randrange(1, t.size() - start)

            movelet = Movelet(trajectory=t, start=start, size=size)

            print(movelet)

            movelets.append(movelet)

        ind = Individual(movelets=movelets, size=size)
        
        population.append(ind)
        
    return population


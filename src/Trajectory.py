
import os, numpy


#  classe ponto
class Point:
    def __init__(self, time, x, y):
        self.x = x
        self.y = y
        self.time = time 
    
    def __repr__(self):
        return "(" + str(self.time) + " , " + str(self.x) + " " + str(self.y) + ")"



# classe trajetoria
class Trajectory:
    def __init__(self, dataset, group):
        self.dataset = dataset
        self.group = group
        self.points = []

    def addPoint(self, p):
        self.points.append(p)

    def size(self):
        return len(self.points)

    def __repr__(self):
        return "(" + str(self.points) + ")"


# retorna a classe da trajetoria com base no nome do arquivo
def getClass(fileName):

    fileName = fileName.replace('.r2', '')
    c = fileName.split(' ')[2]
    
    return {
        #  Hurricane
        'cTS' : "Scale 0",
        'c1' : "Scale 1",
        'c2' : "Scale 2",
        'c3' : "Scale 3",
        'c4' : "Scale 4",
        'c45' : "Scale 4,5",
        #  Animals
        'cC' : "Cattle",
        'cD' : "Deer",
        'cE' : "Elk",
        # Vehicle
        'cB' : "Bus",
        'cT' : "Truck"

    }[c]


# retorna o dataset com base no nome da pasta
def getDataset(d):

    return {
        '1_patel_hurricane_2vs3' : 'Hurricane',
        '2_patel_hurricane_1vs4' : 'Hurricane',
        '3_patel_hurricane_0vs45' : 'Hurricane',
        '4_patel_animals' : 'Animal',
        '5_patel_vehicle' : 'Vehicle',
    }[d]


def read():
    return readFolders()

# TODO: melhorar
# le os arquivos das pastas e retorna as trajetorias 
def readFolders (): 

    foldersName = [
        '1_patel_hurricane_2vs3',
        '2_patel_hurricane_1vs4',
        '3_patel_hurricane_0vs45',
        '4_patel_animals',
        '5_patel_vehicle',
    ]

    experimental = "E1"

    trajectories = []

    for d in foldersName:

        dataset = getDataset(d)

        filePath = "../datasets/" + experimental + "/" + d + '/train'

        t = readFiles(filePath=filePath, dataset=dataset)

        trajectories.extend(t)

    return trajectories


# le os arquivos e monta as trajetorias
def readFiles(filePath, dataset): 

    trajectories = []

    directory = os.fsencode(filePath)

    for file in os.listdir(directory):

        fileName = os.fsdecode(file)

        # print(fileName)

        f = open(filePath + "/" + fileName,"r")

        items = f.readlines()
       
        group = getClass(fileName)

        trajectory = Trajectory(dataset=dataset, group=group)


        # pega os pontos da trajetoria
        for i in items:

            i = i.replace('\n', '')
            s = i.split(',')
            xy = s[1].split(' ')
            p = Point(time=s[0], x=xy[0], y=xy[1])

            trajectory.addPoint(p)

        # print(trajectory.size())

        trajectories.append(trajectory)

    return trajectories

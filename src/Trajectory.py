
import os


#  classe ponto
class Point:
    def __init__(self, time, x, y):
        self.x = x
        self.y = y
        self.time = time 
    
    def __repr__(self):
        return "(" + str(self.time) + " , " + str(self.x) + " " + str(self.y) + ")"

    def getPosition(self):
        return [self.x, self.y]



# classe trajetoria
class Trajectory:
    def __init__(self, fileName, dataset, group, datasetName):
        self.dataset = dataset
        self.group = group
        self.fileName = fileName
        self.datasetName = datasetName
        self.points = []

    def addPoint(self, p):
        self.points.append(p)

    def getPoints(self):
        
        ret = []

        for p in self.points:
            ret.append(p.getPosition())

        return ret

    def size(self):
        return len(self.points)

    def __repr__(self):
        return "(" + str(self.fileName) + ": \t" + str(self.dataset) + " - " + str(self.group) + ")"


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



# le os arquivos das pastas e retorna as trajetorias 
def readDataset (experimental, fileType, datasetName, minSize): 

    # foldersName = [
    #     '1_patel_hurricane_2vs3',
    #     '2_patel_hurricane_1vs4',
    #     '3_patel_hurricane_0vs45',
    #     '4_patel_animals',
    #     '5_patel_vehicle',
    # ]

    trajectories = []

    # for datasetPosition in range(0, len(foldersName)):

    dataset = getDataset(datasetName)

    filePath = "./datasets/" + experimental + "/" + datasetName + '/' + fileType

    t = readFiles(filePath=filePath, dataset=dataset, minSize=minSize, datasetName=datasetName)

    trajectories.extend(t)

    return trajectories


# le os arquivos e monta as trajetorias
def readFiles(filePath, dataset, minSize, datasetName): 

    trajectories = []

    directory = os.fsencode(filePath)

    for file in os.listdir(directory):

        fileName = os.fsdecode(file)

        # print(fileName)

        f = open(filePath + "/" + fileName,"r")

        items = f.readlines()
       
        group = getClass(fileName)

        trajectory = Trajectory(fileName=fileName, dataset=dataset, group=group, datasetName=datasetName)


        # pega os pontos da trajetoria
        for i in items:

            i = i.replace('\n', '')
            s = i.split(',')
            xy = s[1].split(' ')
            p = Point(time=float(s[0]), x=float(xy[0]), y=float(xy[1]))

            trajectory.addPoint(p)

        # print(trajectory.size())

        if trajectory.size() > minSize:
            trajectories.append(trajectory)

    return trajectories


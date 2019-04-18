
import os


#  classe ponto
class Point:
    def __init__(self, t, x, y):
        self.x = x
        self.y = y
        self.t = t 
    
    def __repr__(self):
        return "(" + str(self.t) + " , " + str(self.x) + " " + str(self.y) + ")"



# classe trajetoria
class Trajectory:
    def __init__(self, fileName):
        self.fileName = fileName
        self.points = []

    def addPoint(self, p):
        self.points.append(p)

    def size(self):
        return len(self.points)

    def __repr__(self):
        return "(" + str(self.points) + ")"



# le os arquivos e monta as trajetorias
def readFiles(filePath): 

    trajectories = []

    directory = os.fsencode(filePath)

    for file in os.listdir(directory):

        fileName = os.fsdecode(file)

        # print(fileName)

        f = open(filePath + "/" + fileName,"r")

        items = f.readlines()

        trajectory = Trajectory(fileName=fileName)

        for i in items:

            i = i.replace('\n', '')

            s = i.split(',')

            xy = s[1].split(' ')

            p = Point(t=s[0], x=xy[0], y=xy[1])
            # print(p)

            trajectory.addPoint(p)

        # print(trajectory.size())

        trajectories.append(trajectory)

    return trajectories


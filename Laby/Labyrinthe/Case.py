class Case(object):

    def __init__(self, id, x, y):
        self.id = id

        self.position = (x, y)
        self.mur = 0

    def getPos(self):
        return self.position

    def getNumber(self):
        return self.id

    def getWall(self):
        return self.mur

    def setWall(self, number):
        self.mur += number

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def __str__(self):
        return "{0}/{1}".format(self.id, self.mur)
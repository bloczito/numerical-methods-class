import sys
from random import randint, random
from os import system

from Labyrinthe.Traducteur import *
from Labyrinthe.Case import *


class Labyrinthe(object):

    def __init__(self, tailleX, tailleY):
        self.tailleX = tailleX
        self.tailleY = tailleY

        self.depart = None
        self.arrivee = None

        self.labyrinthe = []
        for i in range(self.tailleX):
            temp = []
            for j in range(self.tailleY):
                temp.append(Case(i * tailleY + j, j, i))
            self.labyrinthe.append(temp)

    def getLab(self):
        return self.labyrinthe

    def getArrive(self):
        return self.arrivee

    def getDepart(self):
        return self.depart

    def getCell(self, x, y):
        try:
            return self.labyrinthe[x][y]
        except IndexError:
            print(x, y)

    def __str__(self):
        retour = ""
        for i in self.labyrinthe:
            retour += "\n"
            for j in i:
                retour += j.__str__() + (" " * (7 - len(j.__str__())))
        return retour

    def afficher(self):
        t = Traducteur(self, self.depart, self.arrivee)
        t.traduire()
        t.afficher(w="███", v="   ")

    def getGroup(self, idCell):
        group = []
        for ligne in range(len(self.labyrinthe)):
            for number in range(len(self.labyrinthe[0])):
                if self.getCell(ligne, number).getNumber() == idCell:
                    group.append(self.getCell(ligne, number))
        return group
    # ==================================================================================================================
    def getCellAround(self, num):

        groupCell = self.getGroup(num)

        group = []
        for cell in groupCell:
            if cell.getPos()[1] < self.tailleX - 1:
                if self.getCell(cell.getPos()[1] + 1, cell.getPos()[0]).getNumber() != num:
                    group.append(self.getCell(cell.getPos()[1] + 1, cell.getPos()[0]))

            if cell.getPos()[1] != 0:
                if self.getCell(cell.getPos()[1] - 1, cell.getPos()[0]).getNumber() != num:
                    group.append(self.getCell(cell.getPos()[1] - 1, cell.getPos()[0]))

            if cell.getPos()[0] < self.tailleY - 1:
                if self.getCell(cell.getPos()[1], cell.getPos()[0] + 1).getNumber() != num:
                    group.append(self.getCell(cell.getPos()[1], cell.getPos()[0] + 1))

            if cell.getPos()[0] != 0:
                if self.getCell(cell.getPos()[1], cell.getPos()[0] - 1).getNumber() != num:
                    group.append(self.getCell(cell.getPos()[1], cell.getPos()[0] - 1))

        return group

    def getNearestCaseInGroupOf(self, case, number):
        """
        :param number:
        :type number: Int
        :param case:
        :type case: Case
        :return:
        """

        group = self.getGroup(number)
        # print("la case choisi est ", case.__str__())
        # print("on retrouve la case de départ parmi: ", [x.__str__() for x in group])

        for p in group:
            if case.getPos()[0] + 1 == p.getPos()[0] and case.getPos()[1] == p.getPos()[1]:
                return p
            if case.getPos()[0] - 1 == p.getPos()[0] and case.getPos()[1] == p.getPos()[1]:
                return p
            if case.getPos()[0] == p.getPos()[0] and case.getPos()[1] + 1 == p.getPos()[1]:
                return p
            if case.getPos()[0] == p.getPos()[0] and case.getPos()[1] - 1 == p.getPos()[1]:
                return p

    def openWall(self, source, destination):

        deltaY = destination.getPos()[0] - source.getPos()[0]
        deltaX = destination.getPos()[1] - source.getPos()[1]

        if deltaX == 0:
            if deltaY == 0:
                print("erreur durant l'ouverture du chemin, les cases sont les même !", file=sys.stderr)
            elif deltaY > 0:
                # mur du bas
                source.setWall(4)
                destination.setWall(1)
                for case in self.getGroup(destination.getId()):
                    case.setId(source.getId())
            else:
                # mur du haut
                source.setWall(1)
                destination.setWall(4)
                for case in self.getGroup(destination.getId()):
                    case.setId(source.getId())
        elif deltaX > 0:
            # mur de droite
            source.setWall(2)
            destination.setWall(8)
            for case in self.getGroup(destination.getId()):
                case.setId(source.getId())
        else:
            # mur de gauche
            source.setWall(8)
            destination.setWall(2)
            for case in self.getGroup(destination.getId()):
                case.setId(source.getId())

    def createOuverture(self, listeOuverture=()):
        """

        :type listeOuverture: Tuple(Int, Int)
        """
        if listeOuverture is None:
            listeOuverture = []
        while True:
            if random() >= 0.5:
                # axeY
                if random() >= 0.5:
                    posX = 0
                    number = 8
                else:
                    posX = self.tailleX - 1
                    number = 2
                posY = randint(0, self.tailleY - 1)
            else:
                # axeX
                if random() >= 0.5:
                    posY = 0
                    number = 1
                else:
                    posY = self.tailleY - 1
                    number = 4
                posX = randint(0, self.tailleX - 1)

            if (posX, posY) not in listeOuverture:
                break

        # print(posX, posY)
        self.getCell(posX, posY).setWall(number)
        return posX, posY

    def step(self):

        number = self.labyrinthe[randint(0, self.tailleX - 1)][randint(0, self.tailleY - 1)].getNumber()
        destination = self.getCellAround(number)

        if len(destination) == 0:
            return
        else:
            destination = destination[randint(0, len(destination) - 1)]
            origine = self.getNearestCaseInGroupOf(destination, number)
            self.openWall(origine, destination)

    # ==================================================================================================================
    def generate(self, stepByStep):

        for i in range(self.tailleX * self.tailleY):
            if stepByStep:
                self.afficher()
                system("pause")

            self.step()

        self.depart = self.createOuverture()
        self.arrivee = self.createOuverture([self.depart])

from CONST import *


class Pathfinder(object):

    def __init__(self, depart, arrivee, plateau):

        self.plateau = plateau
        self.depart = depart
        self.arrivee = arrivee

        self.listeVoisin = []
        self.listeCircuit = [[self.depart]]
        self.circuit = []

    def findGoodPath(self):
        self.findAllPath(0)
        for path in self.listeCircuit:
            if self.arrivee in path:
                self.circuit = path
        return None

    def bindPath(self):
        if len(self.circuit) is None:
            return
        else:
            for cell in self.circuit:
                self.plateau.setCell(cell[1], cell[2], PATH)

    def getValideCell(self, coord):
        self.getVoisin(coord)
        caseValide = []

        for eachCase in self.listeVoisin:
            if eachCase[0] == VOID:
                caseValide.append(eachCase)

        return caseValide if len(caseValide) != 0 else None

    def findAllPath(self, id):
        """
        on verifie si il y a d'autre case dispo
            si non
                on remonte
            si oui, recursivité avec caseActuel sur chacun des cases
                on ajoute a la liste actuelle
        """

        cases = self.getValideCell(self.listeCircuit[id][-1])

        for case in cases:
            if case in self.listeCircuit[id]:
                cases.remove(case)

        # self.plateau.setCell(self.listeCircuit[id][-1][1], self.listeCircuit[id][-1][2], 2)
        # self.plateau.afficher("###", "   ", " . ")
        # self.plateau.setCell(self.listeCircuit[id][-1][1], self.listeCircuit[id][-1][2], 0)

        if len(cases) == 0:
            return
        elif len(cases) == 1:
            self.listeCircuit[id].append(cases[0])
            self.findAllPath(id)
        else:
            for embranchement in cases:
                i = len(self.listeCircuit)
                self.listeCircuit.append(self.listeCircuit[id].copy())
                self.listeCircuit[i].append(embranchement)
                self.findAllPath(i)
            return

    def getVoisin(self, coord):
        self.listeVoisin.clear()

        if coord[1] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] - 1, coord[2])), coord[1] - 1, coord[2]))

        if coord[2] < self.plateau.getTailleY() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1], coord[2] + 1)), coord[1], coord[2] + 1))

        if coord[1] < self.plateau.getTailleX() - 1:
            self.listeVoisin.append(
                (self.plateau.get((coord[1] + 1, coord[2])), coord[1] + 1, coord[2]))

        if coord[2] > 0:
            self.listeVoisin.append(
                (self.plateau.get((coord[1], coord[2] - 1)), coord[1], coord[2] - 1))

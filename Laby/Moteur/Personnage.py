from CONST import *


class Perso(object):

    def __init__(self, moteur, trad, posX, posY):

        self.moteur = moteur
        self.plateau = trad

        self.posX = posX
        self.posY = posY

    def moveUp(self):
        if self.plateau.getCell(self.posX, self.posY + 1) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY + 1, PERSO)
            self.plateau.setCell(self.posX, self.posY, VOID)
            print("up")
            self.posY += 1
            self.moteur.paintGrid()

    def moveDown(self):
        if self.plateau.getCell(self.posX, self.posY - 1) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX, self.posY - 1, PERSO)
            self.plateau.setCell(self.posX, self.posY, VOID)
            print("down")
            self.posY -= 1
            self.moteur.paintGrid()

    def moveLeft(self):
        if self.plateau.getCell(self.posX - 1, self.posY) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX - 1, self.posY, PERSO)
            self.plateau.setCell(self.posX, self.posY, VOID)
            print("left")
            self.posX -= 1
            self.moteur.paintGrid()

    def moveRight(self):
        if self.plateau.getCell(self.posX + 1, self.posY) not in [WALL, ENNEMIE]:
            self.plateau.setCell(self.posX + 1, self.posY, PERSO)
            self.plateau.setCell(self.posX, self.posY, VOID)
            print("right")
            self.posX += 1
            self.moteur.paintGrid()

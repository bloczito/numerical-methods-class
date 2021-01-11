from tkinter import *
from CONST import *
from Labyrinthe import Labyrinthe
from Pathfinder import Pathfinder
from Traducteur import Traducteur
from Personnage import *
from threading import *


class Moteur():
    """inserer de la doc ici"""

    def __init__(self, grid=None):
        self.main = Tk()
        self.main.title("MoteurGraphique")

        if grid is not None and type(grid) == type([]) and type(grid[0]) == type([]):
            self.grid = grid
        else:
            raise (TypeError("Argument grid invalide ou non existant"))

        self.tailleX = len(self.grid) * LARGEUR
        self.tailleY = len(self.grid[0]) * HAUTEUR

        self.main.geometry(str(self.tailleX) + "x" + str(self.tailleY))
        self.main.resizable(True, True)

        self.elements = {}

        self.screen = Canvas(self.main, width=self.tailleX, height=self.tailleY, bg="grey", confine=True)
        self.screen.pack()

        self.paintGrid()

    def getGrid(self):
        return self.grid

    def notify(self, action):
        if action == UPDATE:
            self.paintGrid()


    def paintGrid(self):

        for item in self.screen.find_all():
            self.screen.delete(item)

        posX, posY = 0, 0

        for x in self.grid:
            for y in x:

                if y == WALL:
                    self.screen.create_rectangle(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="black")
                if y == PERSO:
                    self.screen.create_oval(posX, posY, posX + LARGEUR, posY + HAUTEUR, fill="red")
                if y == PATH:
                    self.screen.create_oval(posX + LARGEUR/3, posY + HAUTEUR/3, posX + 2* LARGEUR/3, posY + 2*HAUTEUR/3, fill="blue")
                if y == ENNEMIE:
                    self.screen.create_oval(posX + LARGEUR/3, posY + HAUTEUR/3, posX + 2* LARGEUR/3, posY + 2*HAUTEUR/3, fill="black")

                posX += LARGEUR
            posX = 0
            posY += HAUTEUR

    def run(self):
        self.main.mainloop()


if __name__ == "__main__":
    lab = Labyrinthe(10, 30)
    lab.generate(False)
    trad = Traducteur(lab, lab.getDepart(), lab.getArrive())

    mot = Moteur(trad.getLabTrad())

    trad.addObserver(mot)

    trad.traduire()
    pathfinder = Pathfinder(trad.getDepart(), trad.getArrivee(), trad)
    pathfinder.findGoodPath()
    pathfinder.bindPath()

    mot.run()



import os
import csv
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

import Integrate


class Glass:

    def __init__(self, name=None, tth=None, intensity=None):
        # self.id = os.path.basename(filename).split("_")
        # self.row = returnrow(self.id,Ids)
        self.name = name
        self.tth = tth
        self.intensity = intensity
        self.glassFiles = []
        self.isAmorph = None

    def addfile(self, filename):
        self.glassFiles.append(filename)

    def getintand2theta(self, poniFiles):
        if len(poniFiles) == len(self.glassFiles):
            self.tth, self.intensity = Integrate.integrate(poniFiles, self.glassFiles)
        else:
            print ("The there need to be an equal number of poni and real files")

    def plot(self):
        plt.plot(self.tth, self.intensity)
        axa = plt.axes([0.44, 0.9, 0.15, 0.075])
        axb = plt.axes([0.6, 0.9, 0.15, 0.075])
        axc = plt.axes([0.76, 0.9, 0.15, 0.075])
        bamorph = Button(axa, 'Amorphous')
        bamorph.on_clicked(self.setAmorph)
        bpamorph = Button(axb, 'Partially \n Amorphous')
        bpamorph.on_clicked(self.setPartially)
        bcryst = Button(axc, 'Crystalline')
        bcryst.on_clicked(self.setCryst)
        plt.show()

    def setAmorph(self, event):
        self.isAmorph = "Amorph"
        print (f" {self.name} is set as Amorph = {self.isAmorph}")

    def setPartially(self, event):
        self.isAmorph = "Partially Crystalline"
        print(f" {self.name} is set as Amorph = {self.isAmorph}")

    def setCryst(self, event):
        self.isAmorph = "Crystalline"
        print(f" {self.name} is set as Amorph = {self.isAmorph}")

    def returnrow(self,Ids):
        i=0
        isIn = True
        for Id in Ids:
            print (file)
            if (name == Id.all()):
                isIn = False
                break
            i = i + 1
        if (isIn):
            error = f"The glass with the id {file}is not in the excel sheet"
            print (error)
            raise ValueError(error)
        return i

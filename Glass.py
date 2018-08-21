import os
import csv
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import RectangleSelector


import Integrate


class Glass:

    def __init__(self, name=None, tth=None, intensity=None):
        # self.id = os.path.basename(filename).split("_")
        # self.row = returnrow(self.id,Ids)
        self.name = name
        self.tth = tth
        self.intensity = intensity
        self.glassFiles = []
        self.peakPositions = [[],[]]
        self.isAmorph = None
        self.addpeakon = False

    def addfile(self, filename):
        self.glassFiles.append(filename)


    def getintand2theta(self, poniFiles):
        if len(poniFiles) == len(self.glassFiles):
            self.tth, self.intensity = Integrate.integrate(poniFiles, self.glassFiles)
            self.intensity= self.intensity/max(self.intensity)
        else:
            print ("The there need to be an equal number of poni and real files")

    def plot(self):
        fig = plt.figure()
        axa = plt.axes([0.44, 0.9, 0.15, 0.075])
        axb = plt.axes([0.6, 0.9, 0.15, 0.075])
        axc = plt.axes([0.76, 0.9, 0.15, 0.075])
        #axd = plt.axes([0.1, 0.9, 0.15, 0.075])
        bamorph = Button(axa, 'Amorphous')
        bamorph.on_clicked(self.setAmorph)
        bpamorph = Button(axb, 'Partially \n Amorphous')
        bpamorph.on_clicked(self.setPartially)
        bcryst = Button(axc, 'Crystalline')
        bcryst.on_clicked(self.setCryst)
        #addpeakButton = Button(axd, 'Peak Pick on?\n %s' %self.addpeakon)
        #addpeakButton.on_clicked(self.togglepeakaddon)
        ax = fig.add_subplot(111)

        point = ax.scatter(self.peakPositions[0],self.peakPositions[1], marker="o", color="crimson")
        ax.plot(self.tth, self.intensity)
        plt.axis([20, 80, -0.1, 1.2])
        plt.autoscale(False)


        def addpeak(eclick, erelease):
            x1, y1 = eclick.xdata, eclick.ydata
            x2, y2 = erelease.xdata, erelease.ydata

            mask = (self.tth > min(x1, x2)) & (self.tth < max(x1, x2)) & \
                    (self.intensity > min(y1, y2)) & (self.intensity < max(y1, y2))
            xmasked = self.tth[mask]
            ymasked = self.intensity[mask]
            isInX = list(set(xmasked).intersection(set(self.peakPositions[0])))
            isInY = list(set(ymasked).intersection(set(self.peakPositions[1])))
            print (isInX)
            print(self.peakPositions[0])
            print (isInY)
            if (isInX != [] and isInY != []):
                print(self.peakPositions[0].index(isInX[0]))
                self.peakPositions[0].remove(isInX[0])
                self.peakPositions[1].remove(isInY[0])
                ax.clear()
                ax.plot(self.tth, self.intensity)
                plt.axis([20, 80, -0.1, 1.2])
                plt.autoscale(False)
                for i in range(0, len(self.peakPositions[0])):
                    text = ax.annotate('{:0.2f}\u00b0 '.format(self.peakPositions[0][i]),
                                      (self.peakPositions[0][i]- .6, self.peakPositions[1][i] + .15),
                                       rotation='vertical')
                point = ax.scatter(self.peakPositions[0],
                                   self.peakPositions[1],
                                   marker="o",color="crimson")
                fig.canvas.draw()



            elif len(xmasked) > 0:
                xmax = xmasked[np.argmax(ymasked)]
                ymax = ymasked.max()
                #point.set_data([xmax], [ymax])
                #tx = "xmax: {:.3f}, ymax {:.3f}".format(xmax,ymax)
                self.peakPositions[0].append(xmax)
                self.peakPositions[1].append(ymax)
                point = ax.scatter(self.peakPositions[0],
                                   self.peakPositions[1],
                                   marker="o", color="crimson")
                text = ax.annotate('{:0.2f}\u00b0 '.format(xmax),
                                   (xmax-.65, ymax+.18),
                                   rotation='vertical')
                print(self.peakPositions)
                fig.canvas.draw()

        rs = RectangleSelector(ax, addpeak,
                               drawtype='box', useblit=True, button=[3],
                               minspanx=5, minspany=5, spancoords='pixels',
                               interactive = False)


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

    def togglepeakaddon(self, event):
        if self.addpeakon:
            self.addpeakon = False
        else:
            self.addpeakon = True

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

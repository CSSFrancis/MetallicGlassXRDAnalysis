import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class Glass:
   # ind = 0
    def __init__(self,filename,Ids):
        self.id = os.path.basename(filename).split("_")
        self.row = returnrow(self.id,Ids)
        self.x = getxy(filename)[0]
        self.y = getxy(filename)[1]
        self.isAmorph = None
      #  ind += 1

    def plot (self):
        plt.plot(self.x,self.y)
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

    def setAmorph(self,event):
        self.isAmorph = "Amorph"
        print (f" {self.id} is set as Amorph = {self.isAmorph}")
    def setPartially(self,event):
        self.isAmorph = "Partially Crystalline"
        print(f" {self.id} is set as Amorph = {self.isAmorph}")
    def setCryst (self, event):
        self.isAmorph = "Crystalline"
        print(f" {self.id} is set as Amorph = {self.isAmorph}")



#This function is kind of terrible from a programming prospective
def returnrow(file,Ids):
    position = []
    i=0
    isIn = True
    for Id in Ids:
        #print (f)
        #print (Id)
        if (file == Id):
            isIn = False
            break
        i = i + 1
    if (isIn):
        error = f"The glass with the id {file}is not in the excel sheet"
        print (error)
        raise ValueError(error)
    return i

def getxy(f):
    x, y = [], []
    with open(f, 'r') as load:
        hasHeader = csv.Sniffer().has_header(load.read(1024))
        load.seek(0) #rewind
        reader = csv.reader(load, delimiter=" ")
        if hasHeader:
            next(reader)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x,y
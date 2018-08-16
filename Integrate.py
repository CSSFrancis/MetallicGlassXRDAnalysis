import pyFAI
import fabio

from pyFAI.multi_geometry import MultiGeometry
#import matplotlib.pyplot as plt


from tkinter import filedialog
from tkinter import *

def createMg (aifiles = None):
    if (aifiles == None):
        root = Tk()
        aifiles = filedialog.askopenfilenames(parent=root, title='Choose multiple files')
        aifiles = root.tk.splitlist(aifiles)
        print (aifiles)
        root.destroy()
    ais = []
    for file in aifiles:
        ais.append(pyFAI.load(file))

    mg = MultiGeometry(ais, unit = "2th_deg", radial_range= (25,75)   )
    print (mg)
    return (mg)

def loadImgs (files = None):
    if (files == None):
        root = Tk()
        files = filedialog.askopenfilenames(parent=root, title='Choose multiple files')
        files = root.tk.splitlist(files)
        print (files)
        root.destroy()
    img = []
    for file in files:
        img.append(fabio.open(file).data)
    print (img)
    return img

def integrate(poniFiles = None, Imgs = None):
    mg = createMg(poniFiles)
    imgs = loadImgs(Imgs)

    tth,I = mg.integrate1d(imgs)
    #plt.plot(tth,I)
    #plt.show()
    return tth, I


import os

from tkinter import filedialog
from tkinter import *

import Glass


# A function that takes a file dump, parses the files and then
# outputs and array of glass objects

def integratePlate(filelist):
    filelist = sorted (filelist)
    ponifiles =[]
    glasses = []
    i = -1
    prevname = None
    glass = Glass.Glass()
    for file in filelist:
        base = os.path.basename(file)

        if (os.path.splitext(base)[1]==".poni"):
            ponifiles.append(file)
        elif (os.path.splitext(base)[1]==".gfrm"):
            name = file.split("0")[0]
            print (name)
            if (name != prevname):
                i +=1
                glass = Glass.Glass(name = name)
                glasses.append(glass)
                print (file)
                glasses[i].addfile(file)
                prevname = name
                print (glasses)
                print(i)

            else:
                print(i)
                print (glasses[i])
                print (file)
                glasses[i].addfile(file)
                print(glasses[i].glassFiles)

        else:
            print ("One of the files is not in the right file format")

    for glass in glasses:
        print(glass.glassFiles)
        glass.getintand2theta(ponifiles)
        glass.plot()



    return glasses


root = Tk()
aifiles = filedialog.askopenfilenames(parent=root, title='Choose multiple files')
aifiles = root.tk.splitlist(aifiles)
root.destroy()  
print (aifiles)
glasses =integratePlate(aifiles)


#glasses =integratePlate(('/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample001.gfrm',
#                        '/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample001.poni',
#                         '/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample002.gfrm',
#                         '/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample002.poni',
#                         '/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample003.gfrm',
#                         '/home/carter/Documents/XRDData/Poni Files/XRDFiles/TestSample003.poni')
#)

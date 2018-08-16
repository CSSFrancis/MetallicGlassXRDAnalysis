from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


import pygsheets
from oauth2client.service_account import ServiceAccountCredentials

from Glass import Glass
import numpy as np
from tkinter import filedialog
from tkinter import *

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet. Change for different spreadsheet
# find in the URL
SAMPLE_SPREADSHEET_ID = '1rSe9kO-Aesv1X0qufU5jZtnxxsMri56OvPnOEkaMnP4'
SAMPLE_RANGE_NAME = 'Sheet1!A:J'



def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

# Getting the credentials for my account and Google sheet.  Store credentials as a seperate folder
    gc = pygsheets.authorize(outh_file='client_secret1.json')
    spreadsheet_ID = 'LENS System Trial'
    wks = gc.open(spreadsheet_ID).sheet1
    
    # Call the Sheets API
    Id = []
    Id = np.column_stack((wks.get_col(1, returnas ='matrix'),wks.get_col(2, returnas = 'matrix')))

    #values = result.get('values', [])
    #Id = []
    #for row in values:
     #   Id.append (row[0:2])

    print (Id)
    # Basic File opening.  Supports opening mulitple files
    root = Tk()
    files = filedialog.askopenfilenames(parent=root, title='Choose Poni and XRD measurements')
    files = root.tk.splitlist(files)
    root.destroy()
    Glasses = []

    for f in files:
        Glasses.append(Glass(f,Id))

    for g in Glasses:
        g.plot()


if __name__ == '__main__':
    main()


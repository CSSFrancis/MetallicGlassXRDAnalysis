from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools



import numpy as np
#import pandas as pd
import Functions
from Functions import Glass
import matplotlib.pyplot as plt

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
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1rSe9kO-Aesv1X0qufU5jZtnxxsMri56OvPnOEkaMnP4'
    RANGE_NAME = 'Sheet1!A:J'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    Id = []
    for row in values:
        Id.append (row[0:2])

    print (Id)
    if not values:
        print('No data found.')
    else:
        # Basic File opening.  Supports opening mulitple files
        root = Tk()
        files = filedialog.askopenfilenames(parent=root, title='Choose multiple files')
        files = root.tk.splitlist(files)
        root.destroy()
        Glasses = []

        for f in files:
            Glasses.append(Glass(f,Id))

        for g in Glasses:
            g.plot()


if __name__ == '__main__':
    main()


import pandas as pd
from tkinter import filedialog
import json

from customClasses import Person

def prepareInitialDictionary(tablePath=None):
    if not tablePath:
        tablePath = getTablePath()
    table = pd.read_csv(tablePath, sep=",")
    for column in table.columns:
        table[column] = table[column].str.title()
    table.sort_values(by=['lastName', 'firstName'], inplace=True, ignore_index=True)
    personDict = {}
    for i in range(0, len(table.index)):
        personDict[makeIDstring(i)] = {'firstName': table.loc[i, "firstName"], 'lastName': table.loc[i, "lastName"], 'superlative': table.loc[i, "superlative"], 'id': i}
    with open('personDict.json', 'w') as outfile:
        json.dump(personDict, outfile, indent=4)
    return personDict

def getTablePath():
    tablePath = filedialog.askopenfilename(filetypes=[("Comma-separated values", ".csv")])
    return tablePath

def makeIDstring(n, length=11):
    return "0" * (length - len(str(n))) + str(n)
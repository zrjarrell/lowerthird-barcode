import pandas as pd
from tkinter import filedialog

from customClasses import Person

def prepareInitialDictionary():
    tablePath = getTablePath()
    table = pd.read_csv(tablePath, sep=",")
    for column in table.columns:
        table[column] = table[column].str.title()
    table.sort_values(by=['lastName', 'firstName'], inplace=True, ignore_index=True)
    personDict = {}
    for i in range(0, len(table.index)):
        personDict[makeIDstring(i)] = Person(table.loc[i, "firstName"], table.loc[i, "lastName"], table.loc[i, "superlative"], i)
    return personDict

def getTablePath():
    tablePath = filedialog.askopenfilename(filetypes=[("Comma-separated values", ".csv")])
    return tablePath

def makeIDstring(n, length=11):
    return "0" * (length - len(str(n))) + str(n)
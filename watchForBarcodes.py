
import time

def watchForCodes(personDict):
    while True:
        time.sleep(1)
        code = input("Scan new barcode.")
        code = code[0:11]
        personDict[code].printInfo()
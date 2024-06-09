from prepareDictionary import prepareInitialDictionary
from setupScanner import createConnection
from makeBarcodes import makeBarcodes
from monitorScanner import monitorScanner




personDict = prepareInitialDictionary('/Users/zrj/repos/lowerthird-barcode/sampleTable.csv')
scanner = createConnection('/dev/cu.usbmodem144101')

monitorScanner(scanner)
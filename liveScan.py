from modules.setupScanner import createConnection
from modules.monitorScanner import monitorScanner

scanner = createConnection('/dev/cu.usbmodem144101')

monitorScanner(scanner)
import barcode
from barcode.writer import ImageWriter
from tkinter import filedialog

def makeBarcodes(personDict):
    barcodeDir = filedialog.askdirectory()
    upc = barcode.get_barcode_class('upc')
    for key in personDict:
        newBarcode = upc(key, writer=ImageWriter())
        newBarcode.render(text=personDict[key].fullName()).save(barcodeDir + '/' + key + '.png')
        personDict[key].barcodePath = barcodeDir + '/' + key + '.png'
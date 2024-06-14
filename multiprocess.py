#from queue import Queue
from threading import Thread
from modules.setupScanner import createConnection
from modules.monitorScanner import monitorScanner
from modules.manageQueue import manageQueue, addReadToQueue, queuemasterInput
from modules.customClasses import CustomQueue
import json

f = open('personDict.json',)
personDict = json.load(f)

scanner = createConnection('/dev/cu.usbmodem144101')

#queue = Queue()
queue = CustomQueue()

captureThread = Thread(target=monitorScanner, args=(scanner, queue,))
#executeThread = Thread(target=addReadToQueue, args=(queue, customQ,))
captureThread.start()
#executeThread.start()



import cv2 as cv
import json
from modules.updateImage import updateImage

f = open('personDict.json',)
personDict = json.load(f)

img = cv.imread("lowerthird.tiff")
cv.imshow("image",img)
cv.waitKey(10)
try:
    while True:
        key = queuemasterInput(queue)
        updateImage(personDict, key)
        img=cv.imread("lowerthirdNamed.tiff")
        cv.imshow("image",img)
        cv.waitKey(10)
except KeyboardInterrupt:
    pass

cv.destroyAllWindows()
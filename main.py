import json

f = open('personDict.json',)
personDict = json.load(f)

import shutil
shutil.copyfile('queue_filled.txt', 'queue.txt')
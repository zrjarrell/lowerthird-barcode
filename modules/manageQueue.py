from modules.customClasses import Queue
import os

def manageQueue():
    queue = Queue()
    checkQueueLog(queue)
    try:
        while True:
            print(queue.head)
            if queue.head:
                queuemasterInput(queue)
            checkQueueLog(queue)
    except KeyboardInterrupt:
        pass
    return queue

def checkQueueLog(queue):
    while len(open('queue.txt', 'r').read()) > 0:
        data = open('queue.txt', 'r').read().splitlines(True)
        queue.enqueue(data[0][0:11])
        open('queue.txt', 'w').writelines(data[1:])

def queuemasterInput(queue):
    #os.system('cls' if os.name == 'nt' else 'clear')
    pointer = queue.head
    while pointer:
        print(pointer.key)
        pointer = pointer.next
    userInput = input('Press return to advance queue.') or 'next'
    if userInput == 'next':
        queue.dequeue()

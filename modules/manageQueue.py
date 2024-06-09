from modules.customClasses import Queue

def manageQueue():
    queue = Queue()
    checkQueueLog(queue)
    return queue

def checkQueueLog(queue):
    while len(open('queue.txt', 'r').read()) > 0:
        data = open('queue.txt', 'r').read().splitlines(True)
        queue.enqueue(data[0][0:11])
        open('queue.txt', 'w').writelines(data[1:])
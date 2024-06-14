class Person:
    def __init__(self, firstName, lastName, superlative, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.superlative = superlative
        self.id = idNum

    def fullName(self):
        return self.firstName + " " + self.lastName

    def printInfo(self):
        print(f"\nName: {self.fullName()}\n{self.superlative}\n")

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class CustomQueue:
    def __init__(self, list=None):
        if list:
            for i in range(0, len(list)):
                if i == 0:
                    self.head = Node(list[i])
                    self.tail = self.head
                else:
                    self.tail.next = Node(list[i])
                    self.tail = self.tail.next
        else:
            self.head = None
            self.tail = None

    def saveState(self):
        saveList = []
        while not self.head:
            saveList += self.dequeue()
        return saveList

    def enqueue(self, key):
        if not self.head:
            self.head = Node(key)
            self.tail = self.head
        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            print("No values in queue.")
        else:
            returnValue = self.head.key
            self.head = self.head.next
            return returnValue
        

class Person:
    def __init__(self, firstName, lastName, superlative, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.superlative = superlative
        self.id = idNum

    def fullName(self):
        return self.firstName + " " + self.lastName

    def printInfo(self):
        print(f"Name: {self.fullName()}")
        print(self.superlative)
class person:
    count = 0
    def __init__(self) -> None:
        person.count+=1
        self.count+=1
    @classmethod

    def printCount(self):
        print(self.count)

    def printCount2(self):
        print(self.count)
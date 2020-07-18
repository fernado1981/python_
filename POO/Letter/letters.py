class letters:
    letterList = [0]
    char = ''

    def __init__(self, letter):
        self.letterList = letter

    def showLetters(self):
        print(self.letterList)

    def addLetter(self, character):
        self.char = character
        self.letterList.append(self.char)

    def delLetter(self, character):
        self.char = character
        for i in range(len(self.letterList)):
            if self.char in self.letterList:
                pos = self.letterList.index(self.char)
                del self.letterList[pos]
                break
            else:
                pass

    def countRepitChar(self, character):
        self.char = character
        print(self.letterList.count(self.char))

    def volteoLetter(self):
        self.letterList = self.letterList[::-1]
        print(self.letterList)

    def orderLetter(self):
        self.letterList = self.letterList.sort()

    def minLetter(self):
        for i in range(len(self.letterList)):
            self.letterList[i] = self.letterList[i].lower()

    def mayLetter(self):
        for i in range(len(self.letterList)):
            self.letterList[i] = self.letterList[i].upper()

    def setLetter(self):
        self.letterList = set(self.letterList)

    def arrLetter(self):
        self.letterList = list(self.letterList)
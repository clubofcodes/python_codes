# 1st
class display:
    def __init__(self, FileName):
        refFile = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{FileName}")
        print(refFile.read().upper())
        refFile.close()

FileInput = input("Enter file name : ")
obj = display(FileInput)

# 2nd
class WordList:
    def __init__(self,file):
        self.FileName=file

    def getWordList(self):
        refFile = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{self.FileName}")
        lstWord = list()
        for line in refFile:
            word = line.rstrip().split()
            for element in word:
                if element in lstWord:
                    continue
                else:
                    lstWord.append(element)
        lstWord.sort()
        return lstWord
FileInput = input("Enter file name : ")
obj=WordList(FileInput)
print(obj.getWordList())

# 3rd
class CountWordsAndChars:

    def __init__(self,FileName):
        self.File=FileName
    def getCount(self):
        refFile = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{self.File}")
        lstWord = list()
        lines = 0
        words = 0
        characters = 0
        wordslst = []
        for line in refFile:
            word = line.rstrip().split()
            wordslst = line.split()
            words = words + len(wordslst)
            characters += sum(len(word) for word in wordslst)
        print("Number Of Words : ", words)
        print("Number of Character without spaces : ", characters)

if __name__ == "__main__":
    FileInput = input("Enter file name : ")
    obj=CountWordsAndChars(FileInput)
    obj.getCount()
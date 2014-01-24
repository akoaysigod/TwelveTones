from random import randint

#randomly generate the twelve tone matrix
class GenerateMatrix:
    chromScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self):
        self.primeSeries = []
        self.intervalScale = []

        self.__genPrimeSeries()
        self.__genNumberSeries()
    
        self.currentMatrix = []
    
    def printMatrix(self):
        for row in self.currentMatrix:
            print row

    #generate the prime series to which the rest of the rows will be based on
    def __genPrimeSeries(self):
        self.primeSeries = list(self.chromScale)
        for i in range(11, 0, -1):
            r = randint(0, i)
            tmp = self.primeSeries[i]
            self.primeSeries[i] = self.primeSeries[r]
            self.primeSeries[r] = tmp

    #assign interval distance from reference note to each note in the (prime) series
    def __genNumberSeries(self):
        zero = self.primeSeries[0]

        chrom = []
        zeroIndex = self.chromScale.index(zero)
        for i in range(0, 12):
            note = self.chromScale[zeroIndex % 12]
            zeroIndex += 1
            chrom.append(note)

        for notes in self.primeSeries:
            interval = chrom.index(notes)
            self.intervalScale.append(interval)

    #generate all of the rows and returns the matrix
    def genMatrix(self):
        ret = []
        ret.append(self.primeSeries)

        for i in range(1, 12):
            tmp = []
            classNumber = 12 - int(self.intervalScale[i])
            noteIndex = self.intervalScale.index(classNumber)
            tmp.append(self.primeSeries[noteIndex])
            rootInterval = classNumber

            for k in range(1, 12):
                classNumber = (rootInterval + self.intervalScale[k]) % 12
                noteIndex = self.intervalScale.index(classNumber)
                tmp.append(self.primeSeries[noteIndex])
            ret.append(tmp)
        self.currentMatrix = ret
        return ret

    #if for whatever reason you need to generate a new matrix use this method
    #I don't know if I'll ever need this but I've included it anyway just in case
    def newMatrix(self):
        self.primeSeries[:] = []
        self.intervalScale[:] =[]

        self.__genPrimeSeries()
        self.__genNumberSeries()

        return self.genMatrix()

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note
from random import randint


#randomly generate the prime series
#USAGE:
#generateMatrix = GenerateMatrix()
#matrix = generateMatrix.genMatrix()
class GenerateMatrix:
    chromScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self):
        self.primeSeries = []
        self.intervalScale = []

        self.__genPrimeSeries()
        self.__genNumberSeries()

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
        return ret

    #if for whatever reason you need to generate a new matrix use this method
    #I don't know if I'll ever need this but I've included it anyway just in case
    def newMatrix(self):
        self.primeSeries[:] = []
        self.intervalScale[:] =[]

        self.__genPrimeSeries()
        self.__genNumberSeries()

        return self.genMatrix()



#the following functions generate NoteSeq at random based on rows of the matrix
class RandomMusic:
    def __init__(self, matrix):
        self.workingMatrix = matrix
        self.matrix = list(self.workingMatrix)

    def getRow(self):
        if not self.matrix:
            self.matrix = list(self.workingMatrix)
        row = randint(0, len(self.matrix))
        return self.matrix.pop(row)


    def high(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]
            noteStr = i + str( timing ) + "''"
            note = Note( noteStr )
            melody.append(note)
        return NoteSeq(melody)

    def midHigh(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]

            if (randint(0,1) == 1):
                range = "''"
            else:
                range = ""

            noteStr = i + str( timing ) + range
            note = Note( noteStr )
            melody.append(note)
        return NoteSeq(melody)

    def mid(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]
            noteStr = i + str( timing )
            note = Note( noteStr )
            melody.append(note)
        return NoteSeq(melody)

    def low(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]
            noteStr = i + str( timing ) + ",,"
            note = Note( noteStr )
            melody.append(note)
        return NoteSeq(melody)


#generate the twelve tone matrix
matGen = GenerateMatrix()
matrix = matGen.genMatrix()

#generate the music randomly
music = RandomMusic(matrix)
seqHigh = music.high()
seqMidHigh = music.midHigh()
seqMid = music.mid()
seqBass = music.low()

#generate midi file
midi = Midi(4, 90)
midi.seq_notes(seqHigh, 0)
midi.seq_notes(seqMidHigh, 1)
midi.seq_notes(seqMid, 2)
midi.seq_notes(seqBass, 3)
midi.write('song.mid')


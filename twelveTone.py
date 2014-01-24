from pyknon.genmidi import Midi
from pyknon.music import Note
from pyknon.music import NoteSeq
from pyknon.music import Rest
from genMatrix import GenerateMatrix
from random import *

#the following functions generate NoteSeq at random based on rows of the matrix
class RandomMusic:
    def __init__(self, matrix):
        self.workingMatrix = matrix
        self.matrix = []
        self.currentScale = []

    def getRow(self):
        if not self.matrix:
            self.matrix = list(self.workingMatrix)
        row = randint(0, len(self.matrix) - 1)
        return self.matrix.pop(row)

    def keepSum(self):
        return

    def genNotes(self, octave="''", scale = None):
        if scale is None:
            scale = self.getRow()
        self.currentScale = list(scale)
        totalSum = 0

        length = [4, 8, 16, 32]
        melody = []
        while scale:
            i = scale.pop()

            rest = None
            restDur = length[randint(0, len(length) - 1)]
            noteDur = length[randint(0, len(length) - 1)]

            if random() <= 0.25:
                noteStr = i + str(noteDur) + octave
                rest = Rest(1.0 / restDur)
            else:
                noteStr = i + str(noteDur) + octave

            note = Note(noteStr)
            melody.append(note)

            totalSum += 1.0 / noteDur
            if rest is not None:
                melody.append(rest)
                totalSum += 1.0 / restDur

            if totalSum > 3.75 and length[0] == 4:
                length.pop(0)
            if totalSum > 3.875 and length[0] == 8:
                length.pop(0)
            if totalSum > 3.9375 and length[0] == 16:
                length.pop(0)

            if not scale and totalSum != 4:
                scale = list(self.currentScale)
            elif not scale and totalSum < 4:
                scale = list(self.currentScale)

            if totalSum >= 4:
                break

        return NoteSeq(melody)

    def genRandRange(self, range, scale = None):
        if scale is None:
            scale = self.getRow()
        self.currentScale = list(scale)
        totalSum = 0

        length = [4, 8, 16]
        melody = []

        while scale:
            i = scale.pop()

            randRange = randint(0, len(range) - 1)
            octave = range[randRange]

            rest = None
            restDur = length[randint(0, len(length) - 1)]
            noteDur = length[randint(0, len(length) - 1)]

            if random() <= 0.25:
                noteStr = i + str(noteDur) + octave
                rest = Rest(1.0 / restDur)
            else:
                noteStr = i + str(noteDur) + octave

            note = Note(noteStr)
            melody.append(note)

            totalSum += 1.0 / noteDur
            if rest is not None:
                melody.append(rest)
                totalSum += 1.0 / restDur

            if totalSum > 3.75 and length[0] == 4:
                length.pop(0)
            if totalSum > 3.875 and length[0] == 8:
                length.pop(0)
            if totalSum > 3.9375 and length[0] == 16:
                length.pop(0)

            if not scale and totalSum != 4:
                scale = list(self.currentScale)
            elif not scale and totalSum < 4:
                scale = list(self.currentScale)

            if totalSum >= 4:
                break

        return NoteSeq(melody)


#generate the twelve tone matrix
matGen = GenerateMatrix()
matrix = matGen.genMatrix()

#generate the music randomly
music = RandomMusic(matrix)

highScale = matrix[3]
seqHigh = music.genNotes("''", highScale)
seqMidHigh = music.genRandRange(["'", "''"])

midScale = matrix[7]
seqMid = music.genNotes(",", midScale)

lowScale = matrix[4]
seqBass = music.genNotes(",,", lowScale)

#generate midi file
midi = Midi(4, 90)
midi.seq_notes(seqHigh, 0)
midi.seq_notes(seqMidHigh, 1)
midi.seq_notes(seqMid, 2)
midi.seq_notes(seqBass, 3)

#you'll probably have to change this!
midi.write('/Users/tony/Desktop/song.mid')


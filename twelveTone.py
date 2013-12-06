from pyknon.genmidi import Midi
from pyknon.music import Note
from pyknon.music import NoteSeq
from genMatrix import GenerateMatrix
from random import randint

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
            noteStr = i + str(timing) + "''"
            note = Note(noteStr)
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

            noteStr = i + str(timing) + range
            note = Note(noteStr)
            melody.append(note)
        return NoteSeq(melody)

    def mid(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]
            noteStr = i + str(timing)
            note = Note(noteStr)
            melody.append(note)
        return NoteSeq(melody)

    def low(self):
        scale = self.getRow()

        length = [4, 8, 16]
        melody = []
        for i in scale:
            timing = length[randint(0, 2)]
            noteStr = i + str(timing) + ",,"
            note = Note(noteStr)
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


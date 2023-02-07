import sys
import math

class matrix:
    def __init__(self, string):
        	self.string = string

    def render(self):
        q = math.sqrt(len(self.string))

        i = 1
        matrix = []
        row = []

        for char in self.string:
            row.append(char)
            if(i % q == 0):
                matrix.append(row[::-1] if i % 2 == 0 else row)
                row = []

            i += 1

        print('['+'\n'.join([','.join(['{:1}'.format(item) for item in row]) for row in matrix])+']')

        print(self.string)

if sys.argv[1]:
	s = sys.argv[1]
	matrix(s).render()
else:
	raise Exception('Incorrect data')

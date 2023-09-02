from enum import Enum, auto
import colorama


class Colour(Enum):
	GREY = colorama.Back.BLACK
	YELLOW = colorama.Back.YELLOW
	GREEN = colorama.Back.GREEN
	EMPTY = colorama.Back.RESET

class Guess:
	word : str
	colourPattern : list 

	def __init__(self,word):
		self.word = word
		self.setDefaultPattern()

	def setDefaultPattern(self):
		colour_pattern = []
		for i in range(5):
			colour_pattern.append(Colour.EMPTY)
		self.colourPattern = colour_pattern

	def getColourPattern(self):
		return self.colourPattern
	
	def setColourPattern(self,value):
		self.colourPattern = value

	def getWord(self):
		return self.word

	def setWord(self,value):
		self.word = value
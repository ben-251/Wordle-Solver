from enum import Enum, auto

class Colour(Enum):
	GREY = auto()
	YELLOW = auto()
	GREEN = auto()
	EMPTY = auto()

class Guess:
	word : str
	colourPattern : list # of 5 colours

	def __init__(self,word):
		self.word = word
		self.setDefaultPattern()

	def setDefaultPattern(self):
		colour_pattern = []
		for i in range(5):
			colour_pattern.append(Colour.EMPTY)
		self.colourPattern = colour_pattern

	def getcolourPattern(self):
		return self.colourPattern
	
	def setcolourPattern(self,value):
		self.colourPattern = value

	def getWord(self):
		return self.word

	def setWord(self,value):
		self.word = value
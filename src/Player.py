class Player:
	guesses : list
	def __init__(self):
		self.guesses = []

	def makeGuess(self,options):
		return "adieu"
	
	def setGuesses(self,value):
		self.guesses = value

	def appendGuesses(self,value):
		self.guesses.append(value)

	def getGuesses(self):
		return self.guesses

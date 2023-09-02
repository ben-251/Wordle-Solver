class Player:
	botName: str
	guesses : list
	fileName: str

	def __init__(self):
		self.guesses = []
		self.botName = "default bot"
		self.fileName = "test.txt"

	def getFileName(self):
		return self.fileName

	def makeGuess(self,options):
		return "adieu"
	
	def setGuesses(self,value):
		self.guesses = value

	def appendGuesses(self,value):
		self.guesses.append(value)

	def getGuesses(self):
		return self.guesses

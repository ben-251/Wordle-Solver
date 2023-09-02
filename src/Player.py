from GameDataHandler import GameDataHandler



class Player:
	botName: str
	guesses : list
	fileName: str
	allowedGuesses: list
	possibleWords: list

	def __init__(self):
		self.data_handler = GameDataHandler()
		self.guesses = []
		self.botName = "default bot"
		self.fileName = "test.txt"
		self.allowedGuesses = self.data_handler.getAllowedGuesses()
		self.possibleWords = self.data_handler.getPossibleWords()

	def getFileName(self):
		return self.fileName

	def makeGuess(self):
		return "adieu"
	
	def setGuesses(self,value):
		self.guesses = value

	def appendGuesses(self,value):
		self.guesses.append(value)

	def getGuesses(self):
		return self.guesses

import random

class GameDataHandler:
	__allowedGuesses: list
	__possibleWords: list
	__secretWord: str

	def __init__(self):
		super().__init__()
		self.setWords()
		self.setSecretWord()
		self.completeSetup()

	def getAllowedGuesses(self):
		return self.__allowedGuesses
	
	def getPossibleWords(self):
		return self.__possibleWords
	
	def getSecretWord(self):
		return self.__secretWord

	def setSecretWord(self):
		self.__secretWord = random.choice(self.__possibleWords)


	def setWords(self):
		allowedWordPath = 'data/allowed_guesses.txt'
		possibleWordPath = 'data/possible_words.txt'

		self.__allowedGuesses = self.importWords(allowedWordPath)
		self.__possibleWords = self.importWords(possibleWordPath)

	def importWords(self,filepath: str):
		with open(filepath, "r") as f:
			words = [line.strip() for line in f]		
		return words

	def completeSetup(self):
		print("Setup completed.")

		print(f"secret word is: {self.__secretWord}",
		f"{self.__allowedGuesses[3],self.__possibleWords[3]}"
		)
	
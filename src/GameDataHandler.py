import random
from enum import Enum, auto

class GameStatus(Enum):
	WON = auto()
	LOST = auto()
	IN_PLAY = auto()

class GameDataHandler:
	__allowedGuesses: list
	__possibleWords: list
	__secretWord: str

	def __init__(self):
		super().__init__()
		self.setWords()
		self.setSecretWord()

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

	def updateScores(self,player,game_status):
		file_name = self.createScoreFilePath(self.player.getFileName())
		with open(file_name,"a") as f:
			if game_status == GameStatus.WON:
				f.write(str(len(player.getGuesses()))+"\n")
			else:
				f.write("0\n") #ehhh maybe. could make a constant variable ig

	def createScoreFilePath(self,fileName):
		return f"data/performance_data/{fileName}"

	def createPerformanceFilePath(self,fileName):
		originalPath = self.createScoreFilePath(self.player.getFileName())
		newPath = originalPath[:-3] + "_Analysis.txt"
		return newPath

	def importScores(self):
		scores = []
		file_name = self.createScoreFilePath(self.player.getFileName())
		with open(file_name,"r") as f:
			scores = [line.strip() for line in f]	
			scores = [score for score in scores if score != ""]
		self.scores = scores

	def storeStats(self,stats):
		file_name = self.createPerformanceFilePath(self.player.getFileName())
		with open(file_name,"w") as f:
			f.write(stats)

	def setScores(self,value):
		self.scores = value

	def getScores(self):
		self.importScores()
		return self.scores
	
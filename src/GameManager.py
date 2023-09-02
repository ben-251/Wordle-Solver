from GameDataHandler import GameDataHandler,GameStatus
from Player import Player
from Guess import Guess, Colour
from enum import Enum, auto
from GameDisplay import GameDisplayer

class GameManager(GameDataHandler):
	player: Player
	GameStatus: GameStatus
	GameDisplayer: GameDisplayer

	def __init__(self,player):
		super().__init__()
		self.player = player
		self.GameStatus = GameStatus.IN_PLAY
		self.GameDisplayer = GameDisplayer(self.player)

	def setGameStatus(self,value):
		self.GameStatus = value
	
	def getGameStatus(self):
		return self.GameStatus

	def setPlayer(self,value):
		self.player = value

	def getPlayer(self):
		return self.player

	def play(self):
		game_status = self.getGameStatus()	
		while game_status == GameStatus.IN_PLAY:			
			self.receiveGuess()
			self.findColourPattern()
			self.GameDisplayer.displayFeedback()
			self.updateGameStatus()
			game_status = self.getGameStatus()	
		self.GameDisplayer.display_result(game_status)
		self.updateScores(self.player,game_status)
		return
		
	def receiveGuess(self):
		allowed_guesses = self.getAllowedGuesses()
		guessed_word = self.player.makeGuess(allowed_guesses)
		guess = Guess(guessed_word)

		if not self.isValid(guess):
			print ("invalid guess.")
			return self.receiveGuess()
		self.player.appendGuesses(guess)

	def findColourPattern(self):
		guess = self.player.getGuesses()[-1]
		colour_pattern = self.computeColourPattern(guess)
		guess.setColourPattern(colour_pattern)

	
	def computeColourPattern(self,guess):
		secret_word = self.getSecretWord()
		colour_pattern = []

		for guessed_letter,correct_letter in zip(guess.word,secret_word):
			if guessed_letter not in secret_word:
				colour_pattern.append(Colour.GREY)		
			elif guessed_letter != correct_letter:
				colour_pattern.append(Colour.YELLOW)		
			else:
				colour_pattern.append(Colour.GREEN)						
		return colour_pattern

	def updateGameStatus(self):
		guesses = self.getPlayer().getGuesses()

		if guesses == []:
			self.setGameStatus(GameStatus.IN_PLAY)
			return
		if all(colour == Colour.GREEN for colour in guesses[-1].colourPattern): #interesting idea!
			self.setGameStatus(GameStatus.WON)
			return
		if len(guesses) == 6:
			self.setGameStatus(GameStatus.LOST)
			return
		self.setGameStatus(GameStatus.IN_PLAY)
		return


	def isValid(self,guess):
		if guess.getWord() not in self.getAllowedGuesses():
			return False
		return True

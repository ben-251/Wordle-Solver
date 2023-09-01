from GameDataHandler import GameDataHandler
from Player import Player
from Guess import Guess, Colour

class GameManager(GameDataHandler):
	player: Player
	def __init__(self,player):
		super().__init__()
		self.player = player

	def setPlayer(self,value):
		self.player = value

	def getPlayer(self):
		return self.player

	def play():
		self.checkForWins()

	def getGuess(self):
		guess = Guess(self.player.makeGuess(self.getAllowedGuesses()))
		guess.setWord(self.validateGuess(guess))

		colour_pattern = self.computeColourPattern(guess)
		guess.setColourPattern(colour_pattern)

		print(guess.getColourPattern(),
		f"\nsecret: {self.getSecretWord()}",
		f"\nguess: {guess.getWord()}")
	
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

	def checkForTermination(self):
		guesses = self.getPlayer().getGuesses()

		if all(colour == Colour.GREEN for colour in guesses[-1].colourPattern): #interesting idea!
			return GameStatus.WON
		elif len(guesses) == 6:
			return GameStatus.LOST
		else: 
			return GameStatus.IN_PLAY

	def validateGuess(self,guess):
		if guess.getWord() not in self.getAllowedGuesses():
			print ("invalid guess.")
			return self.getGuess() #I'm not confident that this won't cause any recursion messes
		return guess.getWord()
	
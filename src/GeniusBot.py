from Bot import Bot
from Guess import Colour
import random

class GeniusBot(Bot):
	def __init__(self,thinking_ratio=None):
		super().__init__()
		self.fileName = "genius.txt"
		self.playerName = "Genius"

	def makeGuess(self):
		pass
		
	def getValidGuesses(self,options):
		valid_guesses = []
		elapsed_guesses = [guess.word for guess in self.guesses]
		
		for guess in options:
			if all(letter not in word for word in elapsed_guesses for letter in guess):
				valid_guesses.append(guess)
		return valid_guesses

	
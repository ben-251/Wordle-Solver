from Bot import Bot
from Guess import Colour
import random

class GeniusBot(Bot):
	def __init__(self,thinking_ratio=None):
		super().__init__()
		self.fileName = "genius.txt"
		self.playerName = "Genius"

	def makeGuess(self):
		# for every single word option , and for every single pattern (243) possible from that word option, 
		# find the probability of getting that pattern for that word (number of matches)/total options
		# find the information in bits that you'd get from that pattern
		# multiply the two
		# add to running total (entropy)
		# store the entropy with the word as a tuple
		# sort list of tuples in order of the entropies
		# take the highest one.
		# could also instead keep a running max entropy, so that if the entropy is ever higher, it stores
		# it into max, but otherwise it doesnt bother storing and sorting a hige list
		pass
		
	def getValidGuesses(self,options):
		valid_guesses = []
		elapsed_guesses = [guess.word for guess in self.guesses]
		
		for guess in options:
			if all(letter not in word for word in elapsed_guesses for letter in guess):
				valid_guesses.append(guess)
		return valid_guesses

	
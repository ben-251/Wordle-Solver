from Bot import Bot
from Guess import Colour
import random
import copy

class SmartBot(Bot):
	thinking_ratio: tuple

	def __init__(self,thinking_ratio = None):
		super().__init__()
		self.setThinkingSplit(thinking_ratio)
		self.playerName = f"Smart Bot. {self.thinking_ratio[0]}:{self.thinking_ratio[1]}"
		self.fileName = self.generateFileName()

	def setThinkingSplit(self,ratio):
		if ratio is None:
			ratio = "3:3"

		parts = ratio.split(':')
		numerator = int(parts[0])
		denominator = int(parts[1])

		self.thinking_ratio = (numerator,denominator)

	def generateFileName(self):
		randomGuesses = self.thinking_ratio[0]
		thinkingGuesses = self.thinking_ratio[1]
		return f"smart_bot/{str(randomGuesses)}-{str(thinkingGuesses)}.txt"

	def makeGuess(self):
		randomGuesses = [num + 1 for num in range(self.thinking_ratio[0])]
		current_guess_number = len(self.guesses) + 1

		if current_guess_number in randomGuesses:
			return self.makeRandomGuess()
		return self.makeEducatedGuess()
		
	def makeRandomGuess(self):
		options = copy.deepcopy(self.allowedGuesses)
		random.shuffle(options)

		for guess in options:
			if self.isUnique(guess):
				return guess

		nonUniqueGuess = random.choice(options)
		while nonUniqueGuess in [guess.word for guess in self.guesses]:
			nonUniqueGuess = random.choice(options)
		return nonUniqueGuess

	def isUnique(self,guess):
		elapsed_guesses = [guess.word for guess in self.guesses]
		for letter in guess:
			if any(letter in elapsed_word for elapsed_word in elapsed_guesses):
				return False
		return True

	def makeEducatedGuess(self):
		options = copy.deepcopy(self.allowedGuesses)
		random.shuffle(options)
		for word in options:
			if self.matchesPreviousPatterns(word):
				return word
		return random.choice(options)
		
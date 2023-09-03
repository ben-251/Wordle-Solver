from Bot import Bot
from Guess import Colour
import random

class SmartBot(Bot):
	thinking_ratio: tuple

	def __init__(self,thinking_ratio = None):
		super().__init__()
		self.setThinkingSplit(thinking_ratio)
		self.playerName = f"Smart Bot. {self.thinking_ratio[0]}:{len(self.thinking_ratio[1])}"
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
		options = self.allowedGuesses
		valid_guesses = self.getValidGuesses(options)

		if valid_guesses:
			guess = random.choice(valid_guesses)
		else:
			guess = random.choice(options)
		return guess

	def getValidGuesses(self,options):
		valid_guesses = []
		elapsed_guesses = [guess.word for guess in self.guesses]
		
		for guess in options:
			if all(letter not in word for word in elapsed_guesses for letter in guess):
				valid_guesses.append(guess)
		return valid_guesses

	def makeEducatedGuess(self):
		options = self.allowedGuesses
		true_options = self.findAvailableWords(options)
		return random.choice(true_options)

		
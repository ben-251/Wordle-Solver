from Bot import Bot
from Guess import Colour
import random

class RandomBot(Bot):
	thinking_ratio: tuple

	def __init__(self,thinking_ratio = None):
		super().__init__()
		self.setThinkingSplit(thinking_ratio)
		self.playerName = f"Random Bot. {self.thinking_ratio[0]}:{self.thinking_ratio[1]}"
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
		else:
			return self.makeEducatedGuess()

	def makeRandomGuess(self,elapsed_guesses = None):
		options = self.allowedGuesses
		if elapsed_guesses is None:
			elapsed_guesses = []

		guess = random.choice(options)
		while guess in elapsed_guesses:
			guess = random.choice(options)
		
		return guess

	def makeEducatedGuess(self,elapsed_guesses = None):
		options = self.allowedGuesses

		if elapsed_guesses is None:
			elapsed_guesses = []

		new_guess = self.makeRandomGuess()
		while not self.matchesPreviousPatterns(new_guess):
			elapsed_guesses.append(new_guess)
			new_guess = self.makeRandomGuess(elapsed_guesses=elapsed_guesses)
		return new_guess



		
		
		

		
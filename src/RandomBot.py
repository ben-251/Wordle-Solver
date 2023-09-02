from Bot import Bot
from Guess import Colour
import random

class RandomBot(Bot):
	randomGuesses : list
	thinkingGuesses : list
	yellowLetters : list
	greenLetters : list
	greyLetters : list

	def __init__(self,thinking_ratio = None):
		super().__init__()
		self.botName = f"Random Bot. {len(self.randomGuesses)}:{len(self.thinkingGuesses)}"
		self.fileName = self.generateFileName()

	def generateFileName(self):
		return f"random_bot/{str(len(self.randomGuesses))}-{str(len(self.thinkingGuesses))}.txt"

	def makeGuess(self):
		current_guess_number = len(self.guesses) + 1

		if current_guess_number in self.randomGuesses:
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



		
		
		

		
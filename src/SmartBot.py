from Bot import Bot
from Guess import Colour
import random

class SmartBot(Bot):
	randomGuesses : list
	thinkingGuesses : list
	yellowLetters : list
	greenLetters : list
	greyLetters : list

	def __init__(self,thinking_ratio = None):
		super().__init__()
		self.setThinkingSplit(thinking_ratio)
		self.botName = f"Smart Bot. {len(self.randomGuesses)}:{len(self.thinkingGuesses)}"
		self.fileName = self.generateFileName()

	def generateFileName(self):
		return f"smart_bot/{str(len(self.randomGuesses))}-{str(len(self.thinkingGuesses))}.txt"

	def makeGuess(self):
		current_guess_number = len(self.guesses) + 1

		if current_guess_number in self.randomGuesses:
			return self.makeRandomGuess()
		return self.makeEducatedGuess()

	def makeRandomGuess(self):
		options = self.allowedGuesses
		elapsed_guesses = [guess.word for guess in self.guesses]
		guess = random.choice(options)
		while guess in elapsed_guesses:
			guess = random.choice(options)
		
		for word in elapsed_guesses:
			while any(letter in word for letter in guess):
				guess = random.choice(options)
		return guess

	def makeEducatedGuess(self):
		options = self.possibleWords
		true_options = self.findAvailableWords(options)
		return random.choice(true_options)


		
		
		

		
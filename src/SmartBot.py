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

	# def makeRandomGuess(self):
	# 	options = self.allowedGuesses
	# 	elapsed_guesses = [guess.word for guess in self.guesses]
	# 	guess = random.choice(options)

	# 	if elapsed_guesses == []:
	# 		return guess

	# 	while guess in elapsed_guesses:
	# 		guess = random.choice(options)
		
	# 	invalid = True

	# 	while invalid:
	# 		for word in elapsed_guesses:
	# 			if not any(letter in word for letter in guess):
	# 				invalid = False
	# 			if invalid:
	# 				guess = random.choice(options)
	# 				continue
	# 	return guess

	def makeRandomGuess(self):
		options = self.allowedGuesses
		elapsed_guesses = [guess.word for guess in self.guesses]

		remaining_letters = set(self.allowedGuesses)

		for word in elapsed_guesses:
			remaining_letters -= set(word)

		valid_guesses = [guess for guess in options if all(letter not in word for word in elapsed_guesses for letter in guess)]

		if valid_guesses:
			guess = random.choice(valid_guesses)
		else:
			guess = random.choice(options)

		return guess


	def makeEducatedGuess(self):
		options = self.possibleWords
		true_options = self.findAvailableWords(options)
		return random.choice(true_options)


		
		
		

		
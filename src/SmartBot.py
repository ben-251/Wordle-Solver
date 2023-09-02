from Player import Player
from Guess import Colour
import random

class SmartBot(Player):
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

	def setThinkingSplit(self,ratio):
		if ratio is None:
			ratio = "3:3"

		parts = ratio.split(':')
		numerator = int(parts[0])
		denominator = int(parts[1])
		self.randomGuesses = [num + 1 for num in range(numerator)]
		self.thinkingGuesses = [num + 1 + len(self.randomGuesses) for num in range(denominator)]

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

	def findAvailableWords(self,options):
		available_words = []
		for word in options:
			if self.matchesPreviousPatterns(word):
				available_words.append(word)
		return available_words

	def updateGreyLetters(self):
		grey_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.GREY:
					grey_letters.append((letter,index))
		self.greyLetters = grey_letters

	def updateYellowLetters(self):
		yellow_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.YELLOW:
					yellow_letters.append((letter,index))
		self.yellowLetters = yellow_letters

	def updateGreenLetters(self):
		green_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.GREEN:
					green_letters.append((letter,index))
		self.greenLetters = green_letters

	def matchesPreviousPatterns(self,current_guess):
		self.updateGreenLetters()
		self.updateYellowLetters()
		self.updateGreyLetters()

		if not self.greenLetters == []:
			if any(green_letter[0] not in current_guess for green_letter in self.greenLetters):
				return False
		if not self.yellowLetters == []:
			if any(yellow_letter[0] not in current_guess for yellow_letter in self.yellowLetters):
				return False
		if any(letter[0] in current_guess for letter in self.greyLetters):
				return False		
		for green_letter in self.greenLetters:
			if green_letter[0] != current_guess[green_letter[1]]:
				return False	
		for yellow_letter in self.yellowLetters:
			if yellow_letter[0] == current_guess[yellow_letter[1]]: #might need to also make sure that the yellow letter isnt in green but im not sure
				return False
		return True

		
		
		

		
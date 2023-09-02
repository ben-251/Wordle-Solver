from Player import Player
from Guess import Colour
import random

class RandomBot(Player):
	randomGuesses : list
	thinkingGuesses : list
	yellowLetters : list
	greenLetters : list
	greyLetters : list

	def __init__(self):
		super().__init__()
		self.fileName = "random_bot.txt"
		self.randomGuesses = [1,2,3]
		self.thinkingGuesses = [4,5,6]

	def makeGuess(self,options):
		current_guess_number = len(self.guesses) + 1

		if current_guess_number in self.randomGuesses:
			return makeRandomGuess(self,options)
		else:
			return makeEducatedGuess(self,options)

	def makeRandomGuess(self,options):
		return random.choice(options)

	def makeEducatedGuess(self,options):
		first_guess = self.makeRandomGuess(options)
	
	def updateGreyLetters(self):
		grey_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.GREY:
					grey_letters.append((letter,index))
		return grey_letters

	def updateYellowLetters(self):
		yellow_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.YELLOW:
					yellow_letters.append((letter,index))
		return yellow_letters

	def updateGreenLetters(self):
		green_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.GREEN:
					green_letters.append((letter,index))
		return green_letters

	def matchesPreviousPatterns(self,current_guess):
		self.updateGreenLetters()
		self.updateYellowLetters()
		self.updateGreyLetters()

		for previous_guess in self.guesses:
			if not self.matchesPattern(current_guess, previous_guess):
				return False
		return True

	def matchesPattern(self,current_guess,previous_guess):
		# if the previous word was birds, and im guessing bingo, and the secret word is bored
		# if there are any greens in the pattern for birds, then bingo MUST have the letter there.
		# in this example, birds will be green, grey, green, yellow, grey.

		# so when trying bingo, check that bingo has a b in first position and an r in 3rd.

		# secondly, the yellows must be somewhere in the word. so in this case the word must have a d, 
		# but since we know its not in 4, then it has to have a d in the word, not in d. that means 
		# storing where the letter was found

		# finally, since i and s were grey, make sure those letters arent in the word. 

		# so to make this efficient, i should check for greys first. if ANY grey letters are present ANYWHERE 
		# in the word, then go to the next word.

		# also check if there are any green or yellow letters missing. in other words, if not all the yellow/green letters are in the word
		# then just immediately skip.

		# then if all the green letters are present, check that they match, so like where you found green letters see that 
		# they match. 

		# for yellows, check that the yellows are in a position which is not the current yellow position 
		# and not the green positions

		# if any of the letters in word are in grey letters [done]

		if any(green_letter not in current_guess for green_letter in self.greenLetters[0]):
			return False
		if any(yellow_letter not in current_guess for yellow_letter in self.yellowLetters[0]):
			return False
		if any(letter in self.greyLetters[0] for letter in current_guess):
				return False
		
		
		
		

		
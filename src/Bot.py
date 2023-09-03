from Player import Player
from Guess import Colour
import random

class Bot(Player):
	def __init__(self):
		super().__init__()

	def getColouredLetters(self,target_colour):
		requested_letters = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == target_colour:
					requested_letters.append((letter,index))
		return requested_letters		

	def matchesPreviousPatterns(self,current_guess):
		greenLetters = self.getColouredLetters(Colour.GREEN)
		yellowLetters = self.getColouredLetters(Colour.YELLOW)
		greyLetters = self.getColouredLetters(Colour.GREY)

		if any(green_letter[0] not in current_guess for green_letter in greenLetters):
			return False
		if any(yellow_letter[0] not in current_guess for yellow_letter in yellowLetters):
			return False	
		if any(letter[0] in current_guess for letter in greyLetters):
			return False		
		for green_letter in greenLetters:
			if green_letter[0] != current_guess[green_letter[1]]:
				return False	
		for yellow_letter in yellowLetters:
			if yellow_letter[0] == current_guess[yellow_letter[1]]:
				return False
		return True

	def findAvailableWords(self,options):
		available_words = []
		for word in options:
			if self.matchesPreviousPatterns(word):
				available_words.append(word)
		return available_words

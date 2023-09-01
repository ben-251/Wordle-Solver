from Player import Player

class Human(Player):
	def __init__(self):
		pass

	def makeGuess(self,options):
		return input("Enter a 5-letter word: ")
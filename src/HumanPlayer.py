from Player import Player

class Human(Player):
	def __init__(self):
		super().__init__()
		self.fileName = "human.txt"

	def makeGuess(self):
		return input("Enter a 5-letter word: ")
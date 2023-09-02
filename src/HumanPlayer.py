from Player import Player

class Human(Player):
	def __init__(self,thinking_ratio):
		super().__init__()
		self.fileName = "human.txt"
		self.botName = "Human"

	def makeGuess(self):
		return input("Enter a 5-letter word: ")
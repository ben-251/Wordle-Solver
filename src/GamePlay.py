from Player import Player

class GamePlay:
	player : Player

	def __init__(self):
		pass
	
	def setPlayer(self,value):
		self.player = value

	def getPlayer(self):
		return self.player

	def play():
		pass

	def getGuess(self):
		guess = self.player.guess()
from Player import Player
from GameDataHandler import GameStatus

class GameDisplayer:
	player: Player

	def __init__(self,player):
		self.player = player
	
	def displayFeedback(self):
		guess = self.player.getGuesses()[-1]
		print(guess.getColourPattern(),
		f"\nguess: {guess.getWord()}")
	
	def display_result(self, game_status):
		if game_status == GameStatus.WON:
			print(f"congratulations! you won in {len(self.player.getGuesses())} tries!") #I can't be bothered fixing plurality for 1 try
		elif game_status == GameStatus.LOST:
			print(f"Sorry, your guesses are up.")

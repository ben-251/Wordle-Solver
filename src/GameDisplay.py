from Player import Player
from GameDataHandler import GameStatus
import colorama

class GameDisplayer:
	player: Player

	def __init__(self,player):
		self.player = player
	
	def displayFeedback(self):
		guess = self.player.getGuesses()[-1]

		if self.player.botName == "Human":
			self.displayHumanFeedback()
		else:
			self.displayHumanFeedback()
	
	def displayBotFeedback(self):
		for word in self.player.getGuesses():
			for i in range(5):
				try:
					colour = word.colourPattern[i]
					print(f"{colour.value}_{colorama.Back.RESET}",end = "")
				except IndexError:
					print(f"{colorama.Back.BLACK}______{colorama.Back.RESET}",end = "")
			print("")	
		print("")

	def displayHumanFeedback(self):
		for word in self.player.getGuesses():
			for letter,colour in zip(word.word,word.colourPattern):
				print(f"{colour.value}{letter.upper()}{colorama.Back.RESET}",end = "")
			print("")
		print("")

	def display_result(self, game_status):
		if game_status == GameStatus.WON:
			print(f"Congratulations! you won in {len(self.player.getGuesses())} tries!\n") #I can't be bothered fixing plurality for 1 try
		elif game_status == GameStatus.LOST:
			print(f"Sorry, your guesses are up.\n")

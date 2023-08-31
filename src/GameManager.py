from GameDataHandler import GameDataHandler
from GamePlay import GamePlay

class GameManager(GameDataHandler,GamePlay):
	def __init__(self):
		super().__init__()
		print(f"print #2 the secret word is: {self.getSecretWord()}",
		f"{self.getAllowedGuesses()[3],self.getPossibleWords()[3]}"
		)
	
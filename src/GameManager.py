from GameDataHandler import GameDataHandler
from GamePlay import GamePlay

class GameManager(GameDataHandler,GamePlay):
	def __init__(self):
		super().__init__()
	
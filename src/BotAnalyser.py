from GameManager import GameManager

class BotAnalyser:
	user = None

	def __init__(self,userType):
		self.user = userType

	def runGame(self):
		game_manager = GameManager(self.user())
		print(game_manager.getSecretWord())
		game_manager.play()
	
	def runAnalysis(self,cycleCount=None):
		if cycleCount is None:
			cycleCount = 2

		for i in range(cycleCount):
			self.runGame()
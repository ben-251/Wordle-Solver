from GameManager import GameManager
from GameDataHandler import GameDataHandler

class BotAnalyser:
	user = None
	userType = None
	thinking_ratio = None
	average_score : float
	win_rate : float
	
	def __init__(self,userType,thinking_ratio=None):
		self.thinking_ratio = thinking_ratio
		self.userType = userType
		self.user = userType(thinking_ratio)
		self.game_manager = GameManager(self.user)

	def resetUser(self):
		self.user = self.userType(self.thinking_ratio)

	def runSingleGame(self):
		self.resetUser()
		self.game_manager = GameManager(self.user)
		self.game_manager.play()
	
	def runGames(self,cycleCount=None):
		if cycleCount is None:
			cycleCount = 2

		for i in range(cycleCount):
			self.runSingleGame()
	
	def Analyse(self):
		self.findStatistics()
		self.displayStatistics()
		self.storeStatistics()

	def findStatistics(self):
		scores = self.game_manager.getScores()
		self.average_score = self.findAverageScore(scores)
		self.win_rate = self.findWinRate(scores)
	
	def storeStatistics(self):
		self.game_manager.storeStats(f"Name: {self.user.botName}\nAverage Score: {self.average_score}\nWin Rate: {self.win_rate}%")

	def displayStatistics(self):
		print(f"Name: {self.user.botName}")
		print(f"Average Score: {self.average_score}")
		print(f"Win Rate: {self.win_rate}%")

	def findAverageScore(self,scores):	
		rejected_values = [0,""]
		scores = [int(score) for score in scores if int(score) not in rejected_values]

		if len(scores) == 0:
			return 0

		total = 0
		for number in scores:
			number = int(number)
			total += number
		average_score = round(total/len(scores),2)
		return average_score
	
	def findWinRate(self,scores):
		winTotal = 0
		for number in scores:
			number = int(number)
			if number != 0:
				winTotal += 1

		percentage = round(winTotal/len(scores) * 100,2)
		return percentage
	
	

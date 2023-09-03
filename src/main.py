from BotAnalyser import BotAnalyser
from Player import Player as Default
from HumanPlayer import Human
from RandomBot import RandomBot
from SmartBot import SmartBot

def main():
	runAll()


def runAll():
	for ratio in ["0:6","1:5","2:4","3:3","4:2","5:1"]:
		bot_analyser = BotAnalyser(SmartBot,thinking_ratio=ratio)
		bot_analyser.runGames(cycleCount=20)
		bot_analyser.Analyse()

if __name__ == "__main__":
	main()
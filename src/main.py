from BotAnalyser import BotAnalyser
from Player import Player as Default
from HumanPlayer import Human
from RandomBot import RandomBot

def main():
	bot_analyser = BotAnalyser(Human)
	bot_analyser.runAnalysis()

if __name__ == "__main__":
	main()
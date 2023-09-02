from BotAnalyser import BotAnalyser
from Player import Player
from HumanPlayer import Human

def main():
	bot_analyser = BotAnalyser(Human)
	bot_analyser.runAnalysis()

if __name__ == "__main__":
	main()
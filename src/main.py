from BotAnalyser import BotAnalyser
from Player import Player as Default
from HumanPlayer import Human
from RandomBot import RandomBot
from SmartBot import SmartBot

def main():
	bot_analyser2 = BotAnalyser(RandomBot,thinking_ratio="2:4")
	bot_analyser2.runGames(cycleCount=1)
	bot_analyser2.Analyse()

	bot_analyser3 = BotAnalyser(Human)
	bot_analyser3.runGames(cycleCount=1)
	bot_analyser3.Analyse()

if __name__ == "__main__":
	main()
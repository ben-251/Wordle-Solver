from BotAnalyser import BotAnalyser
from Player import Player as Default
from HumanPlayer import Human
from RandomBot import RandomBot
from SmartBot import SmartBot

def main():
	bot_analyser2 = BotAnalyser(SmartBot,thinking_ratio="0:6")
	bot_analyser2.runGames(cycleCount=100)
	bot_analyser2.Analyse()

	bot_analyser2 = BotAnalyser(SmartBot,thinking_ratio="1:5")
	bot_analyser2.runGames(cycleCount=100)
	bot_analyser2.Analyse()

	bot_analyser2 = BotAnalyser(SmartBot,thinking_ratio="2:4")
	bot_analyser2.runGames(cycleCount=100)
	bot_analyser2.Analyse()

if __name__ == "__main__":
	main()
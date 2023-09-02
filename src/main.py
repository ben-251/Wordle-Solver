from BotAnalyser import BotAnalyser
from Player import Player as Default
from HumanPlayer import Human
from RandomBot import RandomBot
from SmartBot import SmartBot

def main():
	# random_bot = RandomBot(thinking_ratio="3:3")
	# bot_analyser = BotAnalyser(random_bot)
	# bot_analyser.runGames(cycleCount=10)
	# bot_analyser.Analyse()


	# bot_analyser2 = BotAnalyser(RandomBot,thinking_ratio="4:2")
	# bot_analyser2.runGames(cycleCount=25)
	# bot_analyser2.Analyse()

	bot_analyser3 = BotAnalyser(SmartBot,thinking_ratio="1:6")
	bot_analyser3.runGames(cycleCount=25)
	bot_analyser3.Analyse()

if __name__ == "__main__":
	main()
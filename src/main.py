from GameManager import GameManager
from Player import Player
from HumanPlayer import Human

# user = Player()
# game_manager = GameManager(user)
# game_manager.getGuess()

user2 = Human()
game_manager = GameManager(user2)
print(game_manager.getSecretWord())
game_manager.getGuess()
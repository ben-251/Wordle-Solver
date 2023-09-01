from GameManager import GameManager
from Player import Player
from HumanPlayer import Human

# user = Player()
# game_manager = GameManager(user)
# print(game_manager.getSecretWord())
# game_manager.play()

user2 = Human()
game_manager = GameManager(user2)
print(game_manager.getSecretWord())
game_manager.play()
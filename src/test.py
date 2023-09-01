import test_backend as tests
from GameManager import GameManager

def test_game_setup():
	game_manager = GameManager()

	tests.assert_equals(game_manager.getAllowedGuesses()[3],"aarti")
	tests.assert_equals(game_manager.getPossibleWords()[3],"abbey")
	tests.assert_equals(len(game_manager.getSecretWord()),5)

test_game_setup()
import ex11_utils
from game_gui import *
from boggle_board_randomizer import *

class Game:
    """ Handles the boggle game """
    def __init__(self):
        self._letters_matrix = randomize_board(LETTERS)
        self._words_set = ex11_utils.optimize_words_set(
            ex11_utils.load_words_dict("boggle_dict.txt"),
            self._letters_matrix)
        self._boardGUI = None
        self._found_words = set()
        self._score = 0

    def calculate_score(self, path):
        """
        Calculates the score of a single word path
        :param path:
        """
        return len(path) * len(path)

    def on_word_selected(self, coordinates):
        """ Should run when a word is selected by the player.
        Takes the coordinates selected and verifies that the word
        as valid. Then updates the score and the word list. """
        if not ex11_utils.is_valid_path(self._letters_matrix,
                                        coordinates,
                                        self._words_set):
            return
        word = ex11_utils.get_word_by_path(self._letters_matrix, coordinates)
        if word in self._words_set and word not in self._found_words:
            self._score += self.calculate_score(coordinates)
            self._boardGUI.set_score(self._score)
            self._found_words.add(word)
            self._boardGUI.set_words_display(self._found_words)

    def on_game_end(self):
        """
        Should run when the game ends. Restarts the game and creates a
        new one.
        """
        self._letters_matrix = randomize_board(LETTERS)
        self._boardGUI = GameGUI(self.on_word_selected,
                                 self.on_game_end, self._letters_matrix, "Play Again")
        self._score = 0
        self._found_words = set()
        self._words_set = ex11_utils.optimize_words_set(
            ex11_utils.load_words_dict("boggle_dict.txt"),
            self._letters_matrix)
        self._boardGUI.show()

    def run(self):
        """
        Runs boggle.
        """
        self._boardGUI = GameGUI(self.on_word_selected,
                                 self.on_game_end, self._letters_matrix, "Start Game")
        self._boardGUI.show()


if __name__ == "__main__":
    game = Game()
    game.run()








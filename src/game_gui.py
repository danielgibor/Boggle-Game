import tkinter as tki
from typing import Dict

from board import BoardGUI
from word_list_GUI import WordListGUI
from score_GUI import ScoreGUI
from constants import *
from timer_GUI import TimerGUI

GAME_TITLE = "Boggle"


class GameGUI:
    """Handles displaying the boggle game"""
    def __init__(self, on_word_selected, on_game_end,
                 board_matrix, start_button_text):
        self._buttons_to_coords_dict: Dict[tki.Button, tuple] = {}
        self._on_word_selected = on_word_selected
        self._board_matrix = board_matrix
        self._on_game_end = on_game_end
        self._start_button_text = start_button_text
        self._root = tki.Tk()
        self._root.title(GAME_TITLE)
        self._scoreGUI = ScoreGUI()
        self._timerGUI = TimerGUI(self._root, on_game_end)
        self._board_GUI = BoardGUI(on_word_selected,
                                   self._root,
                                   board_matrix)
        self._start_button = None
        self.create_play_button()
        self._word_list_gui = WordListGUI()

    def _create_root(self):
        """Creates the game window"""
        self._root = tki.Tk()
        self._root.title(GAME_TITLE)

    def _destroy_start_button_and_init_game_frame(self):
        """Destroys the start button and starts the actual game"""
        self._start_button.destroy()
        self._init_frames_and_labels()
        self._board_GUI.show(self._outer_frame)
        self._selected_coordinates = []

    def _init_frames_and_labels(self):
        """Initiates all the relevant frames and labels in the game"""
        self._outer_frame = tki.Frame(self._root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._scoreGUI.show(self._outer_frame)
        self._timerGUI.show(self._outer_frame)
        self._word_list_gui.show(self._outer_frame)
        self.set_score(0)

    def create_play_button(self):
        """Creates the button that starts the game"""
        self._start_button = tki.Button(self._root, text=self._start_button_text,
                                        command=self._destroy_start_button_and_init_game_frame,
                                        **BUTTON_STYLE)
        self._start_button.pack()

    def set_score(self, score):
        """Set game score"""
        self._scoreGUI.set_score(score)

    def show(self) -> None:
        """Shows the game"""
        self._root.mainloop()

    def set_words_display(self, words_lst):
        """Sets the word list that was found"""
        self._word_list_gui.set_words_display(words_lst)




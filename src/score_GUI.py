import tkinter as tki

from constants import *

class ScoreGUI:
    """Handles displaying the game score"""
    def __init__(self):
        self._score_label = None

    def show(self, frame):
        """Shows the game score"""
        self._score_label = tki.Label(frame, font=("Courier", 30),
                                      bg=REGULAR_COLOR, width=23, relief="ridge")
        self._score_label.pack(side=tki.TOP, fill=tki.BOTH)

    def set_score(self, score):
        """Sets the game score"""
        self._score_label["text"] = "Score: " + str(score)

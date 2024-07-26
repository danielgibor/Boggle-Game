import tkinter as tki
from constants import *


class TimerGUI:
    """Handles displaying the game timer"""
    def __init__(self, root, on_game_end):
        self._time_display_label = None
        self._root = root
        self._on_game_end = on_game_end

    def show(self, frame):
        """Shows the timer"""
        self._time_display_label = tki.Label(frame,
                                             font=("Courier", 30),
                                             bg=REGULAR_COLOR,
                                             width=4,
                                             relief="ridge")
        self._time_display_label.pack(side=tki.RIGHT, fill=tki.BOTH)
        self.countdown(GAME_TIME_SECONDS)

    def countdown(self, counter):
        """Starts the timer"""
        self._time_display_label['text'] = counter
        if counter > 0:
            self._root.after(1000, self.countdown, counter - 1)
        elif counter == 0:
            self._root.destroy()
            self._on_game_end()

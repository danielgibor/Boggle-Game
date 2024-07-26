import tkinter as tki
from constants import *


class WordListGUI:
    """ Handles displaying the list of words found by the player
      in boggle """

    def __init__(self):
        self._word_list_canvas = None
        self.text_id = None

    def show(self, frame):
        """ Show the word list in the given frame
        :param frame:
        :return:
        """
        self._word_list_canvas = tki.Canvas(frame)
        self._word_list_canvas.pack(side=tki.BOTTOM,
                                    fill=tki.BOTH,
                                    expand=True)
        self.text_id = self._word_list_canvas.create_text(
            10, 10, anchor="nw", text="")

    def set_words_display(self, words_lst):
        """ Display the given word list """
        self.lines_seperator(words_lst)
        self._word_list_canvas.itemconfig(
            self.text_id, text="  ".join(words_lst))

    def lines_seperator(self, words_lst):
        """ Add line separator ever 20 words """
        for i in range(0, len(words_lst), WORDS_LINE_LENGTH):
            if i != 0:
                words_lst[i] = "\n"

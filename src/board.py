import tkinter as tki

from boggle_board_randomizer import BOARD_SIZE
from constants import *

class BoardGUI:
    """Handles displaying the board of letters"""
    def __init__(self, on_word_selected, root, board_matrix):
        self._buttons_to_coords_dict = {}
        self._on_word_selected = on_word_selected
        self._root = root
        self._buttons_frame = None
        self._board_matrix = board_matrix
        self._selected_coordinates = []

    def show(self, frame):
        """Shows the board"""
        self._buttons_frame = tki.Frame(frame)
        self._buttons_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._create_buttons_grid()
        self._initiate_buttons()

    def _create_buttons_grid(self) -> None:
        """Creates the grid where the buttons will be placed"""
        for i in range(BOARD_SIZE):
            tki.Grid.columnconfigure(self._buttons_frame, i, weight=1)

        for i in range(BOARD_SIZE):
            tki.Grid.rowconfigure(self._buttons_frame, i, weight=1)

    def _init_button_bindings(self):
        """Initiates the button bindings"""
        def on_drag(event):
            x, y = self._root.winfo_pointerxy()
            widget_at_coordinate = self._root.winfo_containing(x, y)
            if widget_at_coordinate:
                if widget_at_coordinate in self._buttons_to_coords_dict.keys():
                    widget_at_coordinate.config(bg=BUTTON_ACTIVE_COLOR)
                    coord = self._buttons_to_coords_dict[widget_at_coordinate]
                    if not coord in self._selected_coordinates:
                        self._selected_coordinates.append(
                            self._buttons_to_coords_dict[widget_at_coordinate])

        def on_release(event):
            for button in self._buttons_to_coords_dict.keys():
                button.config(bg=REGULAR_COLOR)
                self._on_word_selected(self._selected_coordinates.copy())
                self._selected_coordinates = []

        self._root.bind('<ButtonPress-1>', on_drag)
        self._root.bind('<B1-Motion>', on_drag)
        self._root.bind('<ButtonRelease-1>', on_release)

    def _initiate_buttons(self):
        """Creates the buttons"""
        self._create_buttons_grid()
        for row_index in range(len(self._board_matrix)):
            for column_index in range(len(self._board_matrix)):
                self._make_button(
                    self._board_matrix[row_index][column_index],
                    row_index, column_index)
        self._init_button_bindings()

    def _make_button(self, button_char, row, col):
        """Creates a single button and places it in the grid"""
        button = tki.Button(self._buttons_frame,
                            text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, sticky=tki.NSEW,
                    padx=5, pady=5)
        self._buttons_to_coords_dict[button] = (row, col)
        return button
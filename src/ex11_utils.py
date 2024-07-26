from boggle_board_randomizer import BOARD_SIZE
TRI_END = "end"


def load_words_dict(filepath):
    """Loads all words from file and returns a set"""
    words_set = set()
    with open(filepath, "r") as f:
        all_words = f.read().splitlines()
        for word in all_words:
            words_set.add(word)
    return words_set


def board_matrix_to_letters_dict(board_matrix):
    """Given a board matrix returns a dict that
    counts the number of appeareances of each letter."""
    letters_dict = {}
    for row in board_matrix:
        for strng in row:
            for letter in strng:
                if letter in letters_dict:
                    letters_dict[letter] += 1
                else:
                    letters_dict[letter] = 1
    return letters_dict


def optimize_words_set(words_set, board_matrix):
    """Given a word set and a boggle board matrix removes
    words that can't appear in the matrix because their
    letters either don't appear in the matrix or the
    letter count is too high"""
    optimized_words_set = set()
    letters_dict = board_matrix_to_letters_dict(board_matrix)
    for word in words_set:
        add_word = True
        for letter in word:
            if letter not in letters_dict:
                add_word = False
                break
            letter_count = word.count(letter)
            if letter_count > letters_dict[letter]:
                add_word = False
                break
        if add_word:
            optimized_words_set.add(word)
    return optimized_words_set


def create_words_tri(words_set):
    tri_root = dict()
    for word in words_set:
        cur_dict = tri_root
        for letter in word:
            cur_dict = cur_dict.setdefault(letter, {})
        cur_dict[TRI_END] = TRI_END
    return tri_root


def is_prefix_in_tri(tri, word):
    cur_dict = tri
    for letter in word:
        if letter not in cur_dict:
            return False
        cur_dict = cur_dict[letter]
    return True


def is_valid_path(board, path, words):
    """Given a path of coordinates in a boggle board
    checks if this path is valid and produces a word
    that appears in the word set"""
    if not _check_path_without_word(board, path):
        return None
    word = get_word_by_path(board, path)
    if word not in words:
        return None
    return word


def _check_path_without_word(board, path):
    """Validates a path in a boggle board without checking
    if the word appears in the dictionary"""
    previous_cells = list()
    for x, y in path:
        if not _check_coordinates_in_board(board, x, y) or not \
                _check_legal_move_to_cell(previous_cells, x, y):
            return False
        previous_cells.append((x, y))
    return True


def _check_coordinates_in_board(board, x, y):
    """Check if coordinates are in the board range"""
    return 0 <= x < len(board) and 0 <= y < len(board[x])


def _check_legal_move_to_cell(previous_cells, x, y):
    """Check if a move from a previous path to a new cell
    is legal"""
    if len(previous_cells) == 0:
        return True
    prev_x, prev_y = previous_cells[-1]
    return (prev_x - 1 <= x <= prev_x + 1) and (prev_y - 1 <= y <= prev_y + 1)\
        and ((x, y) not in previous_cells)


def get_word_by_path(board, path):
    """Gets the word in a given path"""
    word = ""
    for x, y in path:
        word += board[x][y]
    return word


def _find_length_n_paths_helper(n, board, x, y, words, path, result, words_tri):
    """Recursively finds length n paths in a board from the given path"""
    if len(path) > n:
        return
    elif len(path) == n and is_valid_path(board, path, words) and path not in \
            result:
        result.append(path)
        return
    for row in range(x - 1, x + 2):
        for col in [col for col in range(y - 1, y + 2) if
                    _check_path_without_word(board, path + [(row, col)])]:
            new_word = get_word_by_path(board, path + [(row, col)])
            if not (is_prefix_in_tri(words_tri, new_word)):
                continue
            _find_length_n_paths_helper(n, board, row, col, words, path +
                                        [(row, col)], result, words_tri)


def find_length_n_paths(n, board, words):
    """Find all length n paths that produce valid words in
    the given board"""
    if n > BOARD_SIZE * BOARD_SIZE:
        return []
    result = list()
    words_tri = create_words_tri(words)
    for row in range(len(board)):
        for col in range(len(board[row])):
            _find_length_n_paths_helper(n, board, row, col, words,
                                        list(), result, words_tri)
    return result


def _find_length_n_words_helper(n, board, x, y, words,
                                path, word, result, words_tri):
    """Recursively finds length n words in the given board that
    continue the given path"""
    if len(word) > n:
        return
    elif len(word) == n and is_valid_path(
            board, path, words) and path not in \
            result:
        result.append(path)
        return
    for row in range(x - 1, x + 2):
        for col in [col for col in range(y - 1, y + 2) if
                    _check_path_without_word(board, path + [(row, col)])]:
            new_word = get_word_by_path(board, path + [(row, col)])
            if not (is_prefix_in_tri(words_tri, new_word)):
                continue
            _find_length_n_words_helper(n, board, row, col, words, path +
                                        [(row, col)], word + board[row][col],
                                        result, words_tri)


def find_length_n_words(n, board, words):
    """Finds length n words in the given board"""
    if n > BOARD_SIZE*BOARD_SIZE*2:
        return []
    result = list()
    words_tri = create_words_tri(words)
    for row in range(len(board)):
        for col in range(len(board[row])):
            _find_length_n_words_helper(n, board, row, col, words,
                                        list(), "", result, words_tri)
    return result


def max_score_paths(board, words):
    """Returns all paths that produce the maximum score
    for each word."""
    paths_dict = {}
    for n in range(1, BOARD_SIZE*BOARD_SIZE + 1):
        pats = find_length_n_paths(n, board, words)
        for path in pats:
            path_word = get_word_by_path(board, path)
            paths_dict[path_word] = path
    return list(paths_dict.values())

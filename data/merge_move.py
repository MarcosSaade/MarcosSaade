from data.settings import *
from copy import deepcopy


class MergeMove:
    def __init__(self):
        self.board = deepcopy(BOARD_INIT)
        self.previous_board = []

    def move_tiles(self, direction):
        self.previous_board = deepcopy(self.board)

        if direction == 'DOWN':

            """
            This function checks every column separately, i.e [0, 0],[0, 1],[0, 2],[0, 3]; [1, 0],[1, 1],[1, 2] [...]

            -If the move is down, it checks the top three rows to see if a number can merge with the one(s) below
                -It is from top to bottom and searches from the closest position to the farthest
                -For merges not directly below, it checks if there are no numbers between the pair
            -And then if it can be moved (from farther to closest)
            
            -Merged is an array of the numbers which are the result of a merge that happened at this move,
                it helps prevent a bug in which numbers merge twice e.g a right movement for the row [2, 2, 0, 4] would
                produce an 8.
                The array resets for every column.
            """

            # Merge
            for j in [0, 1, 2, 3]:  # for each row
                merged = []  # initialize/reset merged

                for i in [0, 1, 2]:  # for each of the top three numbers, from top to bottom:

                    if i == 0:
                        if self.board[i + 1][j] == self.board[i][j]:  # if num directly below is equal to original num:
                            self.board[i + 1][j] = self.board[i][j] * 2  # double the number directly below
                            self.board[i][j] = 0  # and erase original num
                            merged.append(1)  # now the new number cant merge another time this turn
                        elif self.board[i + 2][j] == self.board[i][j] and self.board[i + 1][j] == 0:
                            self.board[i + 2][j] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i + 3][j] == self.board[i][j] and self.board[i + 1][j] == 0 and \
                                self.board[i + 2][j] == 0:
                            self.board[i + 3][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if i == 1 and i not in merged:
                        if self.board[i + 1][j] == self.board[i][j]:
                            self.board[i + 1][j] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i + 2][j] == self.board[i][j] and self.board[i + 1][j] == 0:
                            self.board[i + 2][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if i == 2 and i not in merged:
                        if self.board[i + 1][j] == self.board[i][j]:
                            self.board[i + 1][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

            # Move
            for i in [2, 1, 0]:
                for j in [0, 1, 2, 3]:

                    if i == 2:
                        if self.board[i + 1][j] == 0:  # if space directly below is empty
                            self.board[i + 1][j] = self.board[i][j]  # copy num below
                            self.board[i][j] = 0  # and erase original num

                    elif i == 1:
                        if self.board[i + 2][j] == 0:
                            self.board[i + 2][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i + 1][j] == 0:
                            self.board[i + 1][j] = self.board[i][j]
                            self.board[i][j] = 0

                    elif i == 0:
                        if self.board[i + 3][j] == 0:
                            self.board[i + 3][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i + 2][j] == 0:
                            self.board[i + 2][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i + 1][j] == 0:
                            self.board[i + 1][j] = self.board[i][j]
                            self.board[i][j] = 0

        if direction == 'UP':

            # Merge
            for j in [0, 1, 2, 3]:
                merged = []

                for i in [3, 2, 1]:

                    if i == 3:
                        if self.board[i - 1][j] == self.board[i][j]:
                            self.board[i - 1][j] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i - 2][j] == self.board[i][j] and self.board[i - 1][j] == 0:
                            self.board[i - 2][j] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(1)
                        elif self.board[i - 3][j] == self.board[i][j] and self.board[i - 1][j] == 0 and \
                                self.board[i - 2][j] == 0:
                            self.board[i - 3][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if i == 2 and i not in merged:
                        if self.board[i - 1][j] == self.board[i][j]:
                            self.board[i - 1][j] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(1)
                        elif self.board[i - 2][j] == self.board[i][j] and self.board[i - 1][j] == 0:
                            self.board[i - 2][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if i == 1 and i not in merged:
                        if self.board[i - 1][j] == self.board[i][j]:
                            self.board[i - 1][j] = self.board[i][j] * 2
                            self.board[i][j] = 0

            # Move
            for i in [1, 2, 3]:
                for j in [0, 1, 2, 3]:

                    if i == 1:
                        if self.board[i - 1][j] == 0:
                            self.board[i - 1][j] = self.board[i][j]
                            self.board[i][j] = 0

                    elif i == 2:
                        if self.board[i - 2][j] == 0:
                            self.board[i - 2][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i - 1][j] == 0:
                            self.board[i - 1][j] = self.board[i][j]
                            self.board[i][j] = 0

                    elif i == 3:
                        if self.board[i - 3][j] == 0:
                            self.board[i - 3][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i - 2][j] == 0:
                            self.board[i - 2][j] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i - 1][j] == 0:
                            self.board[i - 1][j] = self.board[i][j]
                            self.board[i][j] = 0

        if direction == 'RIGHT':

            # Merge
            for i in [0, 1, 2, 3]:  # y
                merged = []

                for j in [0, 1, 2]:  # x

                    if j == 0:
                        if self.board[i][j + 1] == self.board[i][j]:
                            self.board[i][j + 1] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(1)
                        elif self.board[i][j + 2] == self.board[i][j] and self.board[i][j + 1] == 0:
                            self.board[i][j + 2] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i][j + 3] == self.board[i][j] and self.board[i][j + 1] == 0 and self.board[i][
                            j + 2] == 0:
                            self.board[i][j + 3] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if j == 1 and j not in merged:
                        if self.board[i][j + 1] == self.board[i][j]:
                            self.board[i][j + 1] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i][j + 2] == self.board[i][j] and self.board[i][j + 1] == 0:
                            self.board[i][j + 2] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if j == 2 and j not in merged:
                        if self.board[i][j + 1] == self.board[i][j]:
                            self.board[i][j + 1] = self.board[i][j] * 2
                            self.board[i][j] = 0

            # Move
            for j in [2, 1, 0]:
                for i in [0, 1, 2, 3]:

                    if j == 2:
                        if self.board[i][j + 1] == 0:
                            self.board[i][j + 1] = self.board[i][j]
                            self.board[i][j] = 0

                    elif j == 1:
                        if self.board[i][j + 2] == 0:
                            self.board[i][j + 2] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j + 1] == 0:
                            self.board[i][j + 1] = self.board[i][j]
                            self.board[i][j] = 0

                    elif j == 0:
                        if self.board[i][j + 3] == 0:
                            self.board[i][j + 3] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j + 2] == 0:
                            self.board[i][j + 2] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j + 1] == 0:
                            self.board[i][j + 1] = self.board[i][j]
                            self.board[i][j] = 0

        if direction == 'LEFT':

            # Merge
            for i in [0, 1, 2, 3]:  # y
                merged = []

                for j in [3, 2, 1]:  # x

                    if j == 3:
                        if self.board[i][j - 1] == self.board[i][j]:
                            self.board[i][j - 1] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(2)
                        elif self.board[i][j - 2] == self.board[i][j] and self.board[i][j - 1] == 0:
                            self.board[i][j - 2] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(1)
                        elif self.board[i][j - 3] == self.board[i][j] and self.board[i][j - 1] == 0 and self.board[i][
                            j - 2] == 0:
                            self.board[i][j - 3] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if j == 2 and j not in merged:
                        if self.board[i][j - 1] == self.board[i][j]:
                            self.board[i][j - 1] = self.board[i][j] * 2
                            self.board[i][j] = 0
                            merged.append(1)
                        elif self.board[i][j - 2] == self.board[i][j] and self.board[i][j - 1] == 0:
                            self.board[i][j - 2] = self.board[i][j] * 2
                            self.board[i][j] = 0

                    if j == 1 and j not in merged:
                        if self.board[i][j - 1] == self.board[i][j]:
                            self.board[i][j - 1] = self.board[i][j] * 2
                            self.board[i][j] = 0

            # Move
            for j in [1, 2, 3]:
                for i in [0, 1, 2, 3]:

                    if j == 1:
                        if self.board[i][j - 1] == 0:
                            self.board[i][j - 1] = self.board[i][j]
                            self.board[i][j] = 0

                    elif j == 2:
                        if self.board[i][j - 2] == 0:
                            self.board[i][j - 2] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j - 1] == 0:
                            self.board[i][j - 1] = self.board[i][j]
                            self.board[i][j] = 0

                    elif j == 3:
                        if self.board[i][j - 3] == 0:
                            self.board[i][j - 3] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j - 2] == 0:
                            self.board[i][j - 2] = self.board[i][j]
                            self.board[i][j] = 0
                        elif self.board[i][j - 1] == 0:
                            self.board[i][j - 1] = self.board[i][j]
                            self.board[i][j] = 0

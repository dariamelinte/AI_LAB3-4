import copy
import random

from models.directions import Directions

class State:
    def __init__(self):
        self._matrix = list()
        self.last_moved_cell = (10, 10)
        
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

        
    @property
    def last_moved_cell(self):
        return self._last_moved_cell

    @last_moved_cell.setter
    def last_moved_cell(self, last_moved_cell):
        self._last_moved_cell = last_moved_cell

    def initialize_problem_randomly(self):
        sample = random.sample(range(9), 9)

        for idx in range(0, 3):
            row = []
            for number in sample[idx * 3 : (idx + 1) * 3]:
                row.append(number)

            self.matrix.append(row)
        
    def get_empty_cell(self):
        for i, row in enumerate(self.matrix):
            for j, number in enumerate(row):
                if number == 0:
                    return i, j
        return 0, 0

    def is_final(self):
        counter = 1
        for row in self.matrix:
            for number in row:
                if number == 0:
                    continue
                if number != counter:
                    return False
                counter += 1
        return True
    
    def is_valid_move(self, direction):
        zero_cell = self.get_empty_cell()
        moved_cell = self.get_next_pos(zero_cell, direction)
        if moved_cell == self.last_moved_cell or not self.is_valid_cell(moved_cell):
            return False
        return True

    def get_move(self, direction):
        zero_cell = self.get_empty_cell()
        moved_cell = self.get_next_pos(zero_cell, direction)

        if not self.is_valid_move(direction):
            return None
        
        new_state = State()

        new_state.matrix = copy.deepcopy(self.matrix)
        new_state.matrix[zero_cell[0]][zero_cell[1]] = new_state.matrix[moved_cell[0]][moved_cell[1]]
        new_state.matrix[moved_cell[0]][moved_cell[1]] = 0
        new_state.last_moved_cell = zero_cell

        return new_state
    
    @staticmethod
    def get_next_pos(last_moved_cell, direction):
        if direction == Directions.UP:
            return (last_moved_cell[0] - 1, last_moved_cell[1])
        elif direction == Directions.DOWN:
            return (last_moved_cell[0] + 1, last_moved_cell[1])
        elif direction == Directions.LEFT:
            return (last_moved_cell[0], last_moved_cell[1] - 1)
        elif direction == Directions.RIGHT:
            return (last_moved_cell[0], last_moved_cell[1] + 1)

    @staticmethod
    def is_valid_cell(cell):
        if cell[0] < 0 or cell[0] > 2:
            return False
        if cell[1] < 0 or cell[1] > 2:
            return False
        return True
    

    

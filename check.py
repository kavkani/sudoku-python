from typing import List
import math

from typing import List, Set
import math


def is_valid_sudoku(partial_assignment: List[List[int]]):
    def duplicate_check(validation_set: Set[int], i: int, j: int):
        number = partial_assignment[i][j]
        if (number in validation_set):
            return True
        if (number != 0):
            validation_set.add(number)
        return False

    n = len(partial_assignment)
    r = int(math.sqrt(n))

    for i in range(n):
        row_numbers, col_numbers, block_numbers = set(), set(), set()
        for j in range(n):
            if (duplicate_check(row_numbers, i, j) or
                    duplicate_check(col_numbers, j, i) or
                    duplicate_check(block_numbers, (j // r) + r * (i % r), (j % r) + r * (i // r))):
                return False

    return True
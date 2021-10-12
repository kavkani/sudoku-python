from game2dboard import Board
import pygame

n = str(input('satr:'))
m = str(input('sootoon:'))
s = input(input('witch number'))

table1_easy_1 = [
    1, 2, '-',
    2, '-', 1,
    3, 1, '-'
]

table1_easy = [
    1, 2, 3,
    2, 3, 1,
    3, 1, 2
]

b = Board(3, 3)
b[0][0] = 1
b[0][1] = 2
b[0][2] = '-'

b[1][0] = 2
b[1][1] = '-'
b[1][2] = 1

b[2][0] = 3
b[2][1] = 1
b[2][2] = '-'

b.show()
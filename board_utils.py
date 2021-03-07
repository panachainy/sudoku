from solver import solve, valid
from random_number import get_random_number


def get_new_board():
    board_temp = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # print(board_temp)

    for y in range(9):
        for x in range(9):
            # warning: beware infinite loop
            while True:
                new_value = get_random_number(0, 10)
                if is_correct(board_temp, new_value, x, y):
                    board_temp[x][y] = new_value
                    break

    print(board_temp)
    # TODO: change print to return board_temp after done logic
    # return board_temp


def is_correct(board_temp, new_value, x, y):
    return True
    # TODO: add logic here
    # if board_temp[row][col].value == 0:
    #     board_temp[row][col].set(new_value)
    #     self.update_model()

    #     if valid(current_board, new_value, (row, col)) and solve(current_board):
    #         return True
    #     else:
    #         board_temp[row][col].set(0)
    #         board_temp[row][col].set_temp(0)
    #         self.update_model()
    #         return False


get_new_board()

import numpy as np


def read_file(filename):
    with open(filename) as f:
        rows = f.read().splitlines()
        return rows


def mark_current_spot(rows):
    tree_encounters = 0
    row_pos = 0
    col_pos = 0

    row_max = len(rows)
    col_max = len(rows[0])

    while row_pos < row_max-1:

        if (col_pos + 3) < col_max:
            col_pos += 3
        else:
            col_pos = (col_pos - col_max) + 3
        row_pos += 1

        print(rows[row_pos])
        print(rows[row_pos][col_pos])
        if rows[row_pos][col_pos] == '#':
            tree_encounters += 1

        print(rows[row_pos][col_pos])
        print(tree_encounters)
        # print(rows)

if __name__ == '__main__':
    data = np.array(read_file("data3a.txt"))
    mark_current_spot(data)

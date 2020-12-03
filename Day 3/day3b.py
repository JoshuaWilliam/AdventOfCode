right_downs = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2}
]


def read_file(filename):
    with open(filename) as f:
        rows = f.read().splitlines()
        return rows


def mark_current_spot(rows, right, down):
    tree_encounters = 0
    row_pos = 0
    col_pos = 0

    row_max = len(rows)
    col_max = len(rows[0])

    while row_pos < row_max - down:

        if (col_pos + right) < col_max:
            col_pos += right
        else:
            col_pos = (col_pos - col_max) + right
        row_pos += down

        if rows[row_pos][col_pos] == '#':
            tree_encounters += 1

    return tree_encounters


if __name__ == '__main__':
    data = read_file("data3a.txt")
    total_encounters = 1

    for right_down in right_downs:
        right_steps = (right_down.get('right'))
        down_steps = (right_down.get('down'))
        total_encounters *= mark_current_spot(data, right_steps, down_steps)

    print(total_encounters)

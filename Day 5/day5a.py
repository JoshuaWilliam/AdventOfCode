def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        return lines


def get_row(seat):
    lower = 0
    upper = 127
    return calc_final(lower, upper, seat)


def get_column(seat):
    lower = 0
    upper = 7
    return calc_final(lower, upper, seat)


def calc_final(lower, upper, seat):
    for letter in seat:
        if is_upper_half(letter):
            lower = (upper + 1 + lower) / 2
        else:
            upper -= (upper + 1 - lower) / 2
    if lower == upper:
        return lower
    else:
        print('YOU DONE GOOFED')


def is_upper_half(letter):
    if letter == 'B' or letter == 'R':
        return True
    else:
        return False


def get_seat_id(seat):
    row = get_row(seat[:7])
    column = get_column(seat[7:])
    return row * 8 + column


def get_seat_ids(data):
    id_list = [get_seat_id(seat) for seat in data]
    return id_list


if __name__ == '__main__':
    file = read_file('input.txt')
    all_id_s = get_seat_ids(file)
    print(max(all_id_s))


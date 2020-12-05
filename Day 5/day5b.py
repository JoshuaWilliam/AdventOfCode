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
        return int(lower)
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
    seat_ids = get_seat_ids(file)

    id_range = range(min(seat_ids), max(seat_ids) + 1)
    for seat_id in id_range:
        if seat_id not in seat_ids:
            print(seat_id)

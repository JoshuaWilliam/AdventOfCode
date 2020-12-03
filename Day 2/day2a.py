import numpy as np


def read_data(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append(format_string(line.split()))
        return data


def format_string(string):
    pos1, pos2 = string[0].split('-')
    letter = string[1].replace(':', '')
    password = string[2]

    formatted_list = [pos1, pos2, letter, password]
    return formatted_list


def verify_password(policy):
    print(policy)
    pos1 = int(policy[0])
    pos2 = int(policy[1])
    letter = policy[2]
    password = policy[3]
    counter = 0
    print("letter: ", letter)
    print("1: ", password[int(pos1)-1])
    print("2: ", password[int(pos2)-1])

    if (password.count(letter) < pos1) | (password.count(letter) > pos2):
        counter = 0
    else:
        counter = 1

    print(counter)
    print()

    return counter


def count_valid_pws(data):
    counter = 0
    print('data size: ', len(data))
    for policy in data:
        verdict = verify_password(policy)
        counter += verdict
    return counter


if __name__ == '__main__':
    listed = read_data('datad2.txt')
    print(count_valid_pws(listed))

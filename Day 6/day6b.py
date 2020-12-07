def read_file(filename):
    with open(filename) as f:
        return [group.split('\n') for group in f.read().split('\n\n')]


def get_count_in_group(group):
    counts = len(set(group))
    return counts


def get_counts(groups):
    return sum([get_count_in_group(group) for group in groups])


def get_unanimous_counts(groups):
    unique_questions = dict((letter, 0) for letter in set(''.join(el for el in groups)))
    counts = 0

    for group in groups:
        for letter in group:
            unique_questions[letter] += group.count(letter)
            if unique_questions[letter] == len(groups):
                counts += 1
    return counts


def get_total_unanimous(all_groups):
    return sum([get_unanimous_counts(groups) for groups in all_groups])


if __name__ == '__main__':
    data = read_file('test.txt')
    print(get_total_unanimous(data))


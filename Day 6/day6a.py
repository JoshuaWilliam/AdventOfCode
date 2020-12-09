
def read_file(filename):
    with open(filename) as f:
        return [group.replace('\n', '') for group in f.read().split('\n\n')]


def get_count_in_group(group):
    counts = len(set(group))
    return counts


def get_counts(groups):
    return sum([get_count_in_group(group) for group in groups])


if __name__ == '__main__':
    data = read_file('input.txt')
    print(get_counts(data))

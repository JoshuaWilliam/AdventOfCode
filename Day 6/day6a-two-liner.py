with open('test.txt') as f:
    print(sum([len(set(group)) for group in [group.replace('\n', '') for group in f.read().split('\n\n')]]))


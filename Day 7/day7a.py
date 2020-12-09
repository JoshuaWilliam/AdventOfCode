def read_file(filename):
    with open(filename) as f:
        file = f.read().replace('\n', '').split('.')[:-1]
        return file


def create_rules(rule_list):
    total_dict = {}
    [total_dict.update(generate_pairs(rule)) for rule in rule_list]
    return total_dict


def generate_pairs(rules):
    bag_string = ' bag'
    child_start_string = 'contain '

    parent = rules[:(rules.index(bag_string))]
    child = rules[(rules.index(child_start_string) + len(child_start_string)):]
    child_list = [rule[:rule.index(bag_string)] for rule in child.split(', ')]
    child_list = [rule.split(' ', 1) if rule[0].isnumeric() else None for rule in child_list]

    child_dict = {}
    for child_item in child_list:
        if child_item is None:
            child_dict.update()
        else:
            child_bag = child_item[1]
            child_bag_count = int(child_item[0])
            child_dict.update({child_bag: child_bag_count})

    rule = {parent: child_dict}
    return rule


def search_color(bag_color, all_bag_rules):
    bag_list = []

    for bag in all_bag_rules:
        if bag_color in all_bag_rules.get(bag):
            bag_list.append(bag)

    while True:
        if not check_parent_bags(bag_list, all_bag_rules):
            break

    return len(bag_list)


def check_parent_bags(bag_list, all_bag_rules):
    parent_bags = []
    for bag in all_bag_rules:
        if any([containing_bag in all_bag_rules.get(bag) for containing_bag in bag_list]) and bag not in bag_list:
            parent_bags.append(bag)
            bag_list.append(bag)

    if not parent_bags:
        return False
    else:
        return True


if __name__ == '__main__':
    data = read_file('input.txt')
    all_rules = create_rules(data)
    print(search_color('shiny gold', all_rules))


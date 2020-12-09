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


def search_color(bag_color, bag_rules):
    containing_bags = []

    for bag in bag_rules:
        if bag_color in bag_rules.get(bag):
            containing_bags.append(bag)

    while True:
        if not check_bigger_containing_bags(containing_bags, bag_rules):
            break

    return containing_bags


def check_bigger_containing_bags(containing_bags, bag_rules):
    bigger_containing_bags = []
    for bag in bag_rules:
        if any([containing_bag in bag_rules.get(bag) for containing_bag in containing_bags]) and bag not in containing_bags:
            bigger_containing_bags.append(bag)
            containing_bags.append(bag)

    if not bigger_containing_bags:
        return False
    else:
        return True


def check_children_bags(bag, bag_rules):
    # for child in bag_rules[bag]:
    #     print(child)


    return 0


def has_children(bag, bag_rules):
    if bag_rules[bag]:
        return True
    else:
        return False


def calc_total_bags(bag_color, bag_rules):
    parent_bag = bag_rules[bag_color]
    total = 0

    for bag in bag_rules[bag_color]:
        bag_color2 = bag
        current_child = 0
        while has_children(bag_color2, bag_rules):
            calc_total_bags()
            count = parent_bag[bag_color2]
            children = [child for child in bag_rules[bag_color2]]
            total += count * sum(bag_rules[bag].values())




if __name__ == '__main__':
    data = read_file('test.txt')
    all_rules = create_rules(data)
    calc_total_bags("shiny gold", all_rules)


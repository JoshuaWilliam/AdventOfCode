expected_fields = ['byr',
                   'iyr',
                   'eyr',
                   'hgt',
                   'hcl',
                   'ecl',
                   'pid']


def read_file(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n")
        return [line.replace("\n", " ") for line in lines]


def check_fields(passport):
    if all(expected_field in passport for expected_field in expected_fields):
        return 1
    else:
        return 0


def count_valid_passports(passports):
    valid_passports = sum([check_fields(passport) for passport in passports])
    return valid_passports


if __name__ == '__main__':
    data = read_file('input.txt')
    total_valid_passports = count_valid_passports(data)
    print(total_valid_passports)

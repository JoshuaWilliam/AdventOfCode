import re

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


def check_expected_fields(passport):
    if all(expected_field in passport for expected_field in expected_fields):
        return 1
    else:
        return 0


def validate_byr(passport):
    year = int(passport.get('byr'))
    if 1920 <= year <= 2002:
        return True
    else:
        return False


def validate_iyr(passport):
    year = int(passport.get('iyr'))
    if 2010 <= year <= 2020:
        return True
    else:
        return False


def validate_eyr(passport):
    year = int(passport.get('eyr'))
    if 2020 <= year <= 2030:
        return True
    else:
        return False


def validate_hgt(passport):
    height = passport.get('hgt')
    if 'in' in height:
        height = int(height.replace('in', ''))
        if 59 <= height <= 76:
            return True
        else:
            return False

    elif 'cm' in height:
        height = int(height.replace('cm', ''))
        if 150 <= height <= 193:
            return True
        else:
            return False

    else:
        return False


def validate_hcl(passport):
    hair_color = passport.get('hcl')
    if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', hair_color):
        return True
    else:
        return False


def validate_ecl(passport):
    expected_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    eye_color = passport.get('ecl')
    if eye_color in expected_ecl:
        return True
    else:
        return False


def validate_pid(passport):
    passport_id = passport.get('pid')
    if len(passport_id) == 9 and passport_id.isdigit():
        return True
    else:
        return False


def validate_loop(passport):
    for field in expected_fields:
        call_function = ('validate_' + field + '(' + 'passport)')
        if not (eval(call_function)):
            return False
    return True


def validate_fields(passport):
    passport_field_dict = dict([field.split(":") for field in passport.split()])
    if validate_loop(passport_field_dict):
        return 1
    else:
        return 0


def count_valid_passports(passports):
    valid_passports = 0
    for passport in passports:
        if check_expected_fields(passport):
            if validate_fields(passport):
                valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    data = read_file('input.txt')
    total_valid_passports = count_valid_passports(data)
    print(total_valid_passports)

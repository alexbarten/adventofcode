def main():
    print(process_passports('day04/passport_data_0.txt'))


def process_passports(passport_data):
    passport = {}
    valid_passports = 0

    with open(passport_data, 'r') as psp:
        for passport_line in psp:
            line_list = passport_line.split()
            dict_line = dict(kv.split(':') for kv in line_list)
            if dict_line != {}:
                passport.update(dict_line)
            else:
                check = validate_passport(passport)
                if check:
                    valid_passports += 1
                    print(passport)
                passport = {}

    return valid_passports


def validate_passport(passport):
    if passport.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

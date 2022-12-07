def main():
    print(process_passports('day04/passport_data_1.txt'))


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
                if validate_passport(passport):
                    valid_passports += 1
                passport = {}

    if validate_passport(passport):
        valid_passports += 1
    return valid_passports


def validate_passport(passport):
    if passport.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
        pass
    else:
        return False

    if int(passport.get('byr')) < 1920 or int(passport.get('byr')) > 2002:
        return False

    if int(passport.get('iyr')) < 2010 or int(passport.get('iyr')) > 2020:
        return False

    if int(passport.get('eyr')) < 2020 or int(passport.get('eyr')) > 2030:
        return False

    length = passport.get('hgt')
    if length[-2:] == 'cm':
        cm = int(length.split('cm')[0])
        if cm < 150 or cm > 193:
            return False
    elif length[-2:] == 'in':
        inch = int(length.split('in')[0])
        if inch < 59 or inch > 76:
            return False
    else:
        return False

    hcl = passport.get('hcl')
    if hcl[0] != '#':
        return False
    if len(hcl) != 7:
        return False
    for i in range(1, 7):
        if hcl[i] not in ('0','1','2','3','4','5','6','7','8','9') and\
              hcl[i] not in ('a','b','c','d','e','f'):
            return False

    if passport.get('ecl') not in ('amb','blu','brn','gry','grn','hzl','oth'):
        return False

    if len(passport.get('pid')) != 9:
        return False
    try:
        i = int(passport.get('pid'))
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    main()

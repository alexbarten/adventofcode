def main():
    print('Valid passwords: ', count_valid_passwords('day02/passwords_1.txt'))


def count_valid_passwords(passwords):
    """count_valid_passwords

    Count the number of valid passwords in the file, which has the following
    structure:

    '<pos1>-<pos2> <c>: <password>'

    - <pos1>: position 1 of occurrence of character 'c' in the password.
    - <pos2>: position 2 of occurrence of character 'c' in the password.
        In both cases the position represents a base-1 number.
    - <c>: the character that the rule is about.
    - <password>: a password that the rule needs to be applied to.

    Args:
        passwords (text file): file of passwords and their rules (one
        definition per line).

    Returns:
        int: valid_password_count
    """
    valid_password_count = 0
    with open(passwords, 'r') as passwordlist:
        for pwline in passwordlist:
            checkchar = pwline.split(' ')[1]
            checkchar = checkchar[0]
            password = pwline.split(' ')[2]

            positions = pwline.split(' ', 1)
            pos1, pos2 = positions[0].split('-')

            pos1 = int(pos1) - 1
            pos2 = int(pos2) - 1

            if checkchar == password[pos1] or checkchar == password[pos2]:
                if password[pos1] != password[pos2]:
                    valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    main()

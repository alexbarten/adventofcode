def main():
    print('Valid passwords: ', count_valid_passwords('day02/passwords_1.txt'))


def count_valid_passwords(passwords):
    """count_valid_passwords

    Count the number of valid passwords in the file, which has the following
    structure:

    '<min>-<max> <c>: <password>'

    - <min>: minimum number of occurrences of character 'c' in the password.
    - <max>: maximum number of occurrences of character 'c' in the password.
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
            countchar = pwline.split(' ')[1]
            countchar = countchar[0]
            password = pwline.split(' ')[2]
            counted = password.count(countchar)

            minmax = pwline.split(' ', 1)
            min, max = minmax[0].split('-')

            if counted >= int(min) and counted <= int(max):
                valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    main()

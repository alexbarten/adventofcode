def main():
    print('Valid passwords: ', count_valid_passwords('day02/passwords_0.txt'))


def count_valid_passwords(passwords):
    """count_valid_passwords

    Count the number of valid passwords in the file, which has the following
    structure:

    'nnn c: password'

    - nnn: number of occurrences of character 'c' in the password, where
    position 1 is the lower occurrence boundary, and position 3 the higher.
    - c: the character that the rule is about.
    - password: a password that the rule needs to be applied to.

    Args:
        passwords (text file): file of passwords and their rules (one
        definition per line).

    Returns:
        int: valid_password_count
    """
    valid_password_count = 0
    with open(passwords, 'r') as passwordlist:
        for pwline in passwordlist:
            counted = pwline.count(pwline[4])
            counted -= 1  # deduct the search character itself

            if counted >= int(pwline[0]) and counted <= int(pwline[2]):
                valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    main()

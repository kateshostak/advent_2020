import re


def is_valid(passport):
    try:
        return all(

                [
                    passport['byr'] >= '1920', passport['byr'] <= '2020',
                    passport['iyr'] >= '2010', passport['iyr'] <= '2020',
                    passport['eyr'] >= '2020', passport['eyr'] <= '2030',

                    any(
                        [
                            all([passport['hgt'][-2:] == 'in', passport['hgt'][:-2] >= '59', passport['hgt'][:-2] <= '76']),
                            all([passport['hgt'][-2:] == 'cm', passport['hgt'][:-2] >= '150', passport['hgt'][:-2] <= '193'])
                        ]),
                    re.match('#[0-9a-f]{6}', passport['hcl']),
                    passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                    len(passport['pid']) == 9
                ]
            )

    except KeyError:
        return False


def main():
    res = 0
    with open('4_a.txt') as f:
        line = -1
        passport = {}
        while line:
            line = f.readline()
            if line == '\n' or line == '':
                if is_valid(passport):
                    res += 1
                passport = {}
                continue

            for field in line.strip('\n').split(' '):
                key, val = field.split(':')
                passport[key] = val
    print(res)


if __name__ == '__main__':
    main()

import re


required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse(file_):
    lines = map(lambda s:  s.replace('\n', ' ').strip(), filter(None, file_.split('\n\n')))
    passports = []
    for l in lines:
        tmp_pass = {}
        l = [elem for elem in l.split(' ')]
        print(l)
        for elem in l:
            k, v = elem.split(':')
            tmp_pass[k] = v
        passports.append(tmp_pass)
    return passports


def solution(passports):
    res = 0
    for elem in passports:
        if got_all_fields(elem) and is_valid(elem):
            res += 1

    return res


def got_all_fields(passport):
    return all([f in passport for f in required])


def is_valid(passport):
    return all([
        len(passport['byr']) == 4 and passport['byr'].isdigit() and passport['byr'] >= '1920' and passport['byr'] <= '2020',
        len(passport['iyr']) == 4 and passport['iyr'].isdigit() and passport['iyr'] >= '2010' and passport['iyr'] <= '2020',
        len(passport['eyr']) == 4 and passport['eyr'].isdigit() and passport['eyr'] >= '2020' and passport['eyr'] <= '2030',
        any([
            passport['hgt'][-2:] == 'in' and passport['hgt'][:-2] >= '59' and passport['hgt'][:-2] <= '76',
            passport['hgt'][-2:] == 'cm' and passport['hgt'][:-2] >= '150' and passport['hgt'][:-2] <= '193'
            ]),
        re.match('#[0-9a-f]{6}', passport['hcl']),
        passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        len(passport['pid']) == 9
        ])


def main():
    with open('4_a.txt') as f:
        print(solution(parse(f.read())))


if __name__ == '__main__':
    main()

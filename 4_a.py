

def main():
    res = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open('4_a.txt') as f:
        line = -1
        passport = {}
        i = 0
        while line:
            line = f.readline()
            if line == '\n' or line == '':
                if all(f in passport for f in fields):
                    res += 1
                passport = {}
                continue

            for field in line.strip('\n').split(' '):
                key, val = field.split(':')
                passport[key] = val
    print(res)


if __name__ == '__main__':
    main()

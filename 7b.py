import sys


def parse(f):
    luggage = {}
    for line in f:
        k, v = line.strip('.\n').split(' contain ')
        key = k.split(' ')
        vals = []
        for val in v.split(', '):
            tmp = [elem for elem in val.split(' ')]
            if tmp[0].isdigit():
                n = int(tmp[0])
            else:
                n = 0
            vals.append([' '.join(tmp[1:-1]), n])
        luggage[' '.join(key[:-1])] = vals
    return luggage


def solution(data, elem):
    return 0 if elem not in data or elem == 'other' else sum(el[1] * solution(data, el[0]) + el[1] for el in data[elem])


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        path = '7test.txt'
    else:
        path = '7.txt'
    with open(path) as f:
        print(solution(parse(f), "shiny gold"))


main()

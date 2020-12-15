from collections import defaultdict


def parse(f):
    inpt = [int(elem) for elem in f.strip().split('\n')]
    inpt.append(0)
    inpt.append(max(inpt) + 3)
    return inpt


def solution(inpt):
    d = defaultdict(int)
    d[max(inpt)] = 1
    for elem in sorted(inpt[:-1], reverse=True):
        d[elem] = d[elem + 1] + d[elem + 2] + d[elem + 3]
    return d[0]


def main():
    with open('10.txt') as f:
        print(solution(parse(f.read())))


main()

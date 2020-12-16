def parse(f):
    n = int(f[0])
    return [n, map(int, filter(lambda s: s != 'x', f[1].strip('\n').split(',')))]


def solution(inpt):
    res = []
    for id_ in inpt[1]:
        a = inpt[0] // id_
        if inpt[0] % id_ != 0:
            a += 1
        min_ = abs(id_*a - inpt[0])
        res.append([id_, min_])
    v = min(res, key=lambda s: s[1])
    return v[0]*v[1]


def main():
    with open('13.txt') as f:
        print(solution(parse(f.readlines())))


main()

from collections import Counter


def parse(file_):
    return filter(None, file_.split('\n\n'))


def solution(forms):
    res = 0
    for group in forms:
        tmp = Counter()
        lines = group.strip().split('\n')
        for line in lines:
            tmp.update(list(line))
        for k, v in tmp.items():
            if v == len(lines):
                res += 1

    return res


def main():
    with open('6.txt') as f:
        print(solution(parse(f.read())))


if __name__ == '__main__':
    main()

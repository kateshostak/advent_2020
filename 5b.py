def parse(file_):
    return [line for line in file_.strip().split('\n')]


def solution(passes):
    ids = []
    for p in passes:
        row = int(p[:-3].replace('F', '0').replace('B', '1'), 2)
        column = int(p[-3:].replace('R', '1').replace('L', '0'), 2)
        ids.append(row * 8 + column)
    ids.sort()
    for i in range(0, len(ids) - 1):
        if (ids[i + 1] - ids[i]) > 1:
            return ids[i] + 1


def main():
    with open('5.txt') as f:
        print(solution(parse(f.read())))


if __name__ == '__main__':
    main()

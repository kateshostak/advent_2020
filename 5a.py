def parse(file_):
    return [line for line in file_.strip().split('\n')]


def solution(passes):
    max_id = 0
    for p in passes:
        row = int(p[:-3].replace('F', '0').replace('B', '1'), 2)
        column = int(p[-3:].replace('R', '1').replace('L', '0'), 2)
        max_id = max(row * 8 + column, max_id)
    return max_id


def main():
    with open('5.txt') as f:
        print(solution(parse(f.read())))


if __name__ == '__main__':
    main()

def parse(file_):
    return filter(None, file_.split('\n\n'))


def solution(forms):
    res = 0
    for group in forms:
        tmp = set()
        for elem in filter(None, group.split('\n')):
            for letter in elem:
                tmp.add(letter)
        res += len(tmp)

    return res


def main():
    with open('6.txt') as f:
        print(solution(parse(f.read())))


if __name__ == '__main__':
    main()

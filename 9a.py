def parse(f):
    return [int(elem) for elem in f.strip().split()]


def solution(inpt):
    for i in range(26, len(inpt)):
        if not is_valid(i, inpt):
            return inpt[i]


def is_valid(k, inpt):
    for i in range(k - 25, k):
        for j in range(i, k):
            if inpt[k] == inpt[i] + inpt[j]:
                return True
    return False


def main():
    with open('9.txt') as f:
        print(solution(parse(f.read())))


main()

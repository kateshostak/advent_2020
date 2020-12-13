def parse(f):
    return [int(elem) for elem in f.strip().split()]


def solution(inpt):
    n = find_number(inpt)
    i = 0
    j = 1
    sum_ = inpt[0] + inpt[1]
    while True:
        if sum_ == n:
            return min(inpt[i:j + 1]) + max(inpt[i:j + 1])

        if sum_ > n:
            sum_ -= inpt[i]
            i += 1
        else:
            j += 1
            sum_ += inpt[j]


def find_number(inpt):
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

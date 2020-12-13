def parse(f):
    return [int(elem) for elem in f.strip().split('\n')]


def solution(inpt):
    jlt_1 = 0
    jlt_3 = 1
    inpt.sort()
    if inpt[0] < 3:
        jlt_1 = 1
    else:
        jlt_3 = 2
    for i in range(len(inpt) - 1):
        if inpt[i + 1] - inpt[i] == 3:
            jlt_3 += 1
        elif inpt[i + 1] - inpt[i] == 1:
            jlt_1 += 1
    return jlt_1 * jlt_3


def main():
    with open('10.txt') as f:
        print(solution(parse(f.read())))


main()

def parse(f):
    inpt = [int(elem) for elem in f.strip().split('\n')]
    inpt.append(0)
    inpt.append(max(inpt) + 3)
    inpt.sort()
    w = {}
    for i, elem in enumerate(inpt):
        w[elem] = []
        j = i + 1
        while j < len(inpt) and inpt[j] - elem <= 3:
            w[elem].append(inpt[j])
            j += 1
    return w


def solution(inpt):
    def traverse(elem):
        if elem == 49:
            return 1

        res = 0
        for el in inpt[elem]:
            res += traverse(el)
        return res
    print(traverse(0))



def main():
    with open('10test.txt') as f:
        print(solution(parse(f.read())))


main()

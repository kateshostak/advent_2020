def parse(f):
    luggage = {}
    for line in f:
        k, v = line.strip('.\n').split(' contain ')
        key = k.split(' ')
        vals = []
        for val in v.split(', '):
            tmp = [elem for elem in val.split(' ') if not elem.isdigit()]
            vals.append(' '.join(tmp[:-1]))
        luggage[' '.join(key[:-1])] = vals
    return luggage


def solution(data):
    def traverse(elem):
        if elem not in data or elem == 'no other':
            return 0

        for el in data[elem]:
            if el == 'shiny gold':
                return 1
            if traverse(el):
                return 1
        return 0

    count = 0
    for key in data:
        count += traverse(key)
    return count


def main():
    with open('7.txt') as f:
        print(solution(parse(f)))


main()

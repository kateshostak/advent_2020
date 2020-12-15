import copy


def parse(f):
    return [list(line) for line in f.strip().split('\n')]


def solution(inpt):
    changed = True

    new_inpt = copy_matrix(inpt)
    while changed:
        changed = do_round(inpt, new_inpt)
        inpt = copy_matrix(new_inpt)
    return count_occupied(new_inpt)


def count_occupied(inpt):
    count = 0
    for line in inpt:
        for elem in line:
            count += 1 if elem == '#' else 0
    return count


def copy_matrix(source):
    dest = []
    for i in range(len(source)):
        dest.append(copy.copy(source[i]))
    return dest


def do_round(inpt, new_inpt):
    changed = False
    for i in range(len(inpt)):
        for j in range(len(inpt[i])):
            if step(i, j, inpt, new_inpt):
                changed = True
    return changed


def step(i, j, inpt, new_inpt):
    if inpt[i][j] == 'L':
        if adjacent_empty(i, j, inpt):
            new_inpt[i][j] = '#'
            return True
    elif inpt[i][j] == '#':
        if adjacent_full(i, j, inpt):
            new_inpt[i][j] = 'L'
            return True
    return False


def adjacent_full(i, j, inpt):
    count = 0
    if i - 1 > 0:
        if j - 1 > 0 and inpt[i - 1][j - 1] == '#':
            count += 1
        if inpt[i - 1][j] == '#':
            count += 1
        if j + 1 < len(inpt[0]) and inpt[i - 1][j + 1] == '#':
            count += 1

    if j - 1 > 0 and inpt[i][j - 1] == '#':
        count += 1
    if j + 1 < len(inpt[0]) and inpt[i][j + 1] == '#':
        count += 1

    if i + 1 < len(inpt):
        if j - 1 > 0 and inpt[i + 1][j - 1] == '#':
            count += 1
        if inpt[i + 1][j] == '#':
            count += 1
        if j + 1 < len(inpt[0]) and inpt[i + 1][j + 1] == '#':
            count += 1
    return count >= 4


def adjacent_empty(i, j, inpt):
    if i - 1 > 0:
        if j - 1 > 0 and inpt[i - 1][j - 1] == '#':
            return False
        if inpt[i - 1][j] == '#':
            return False
        if j + 1 < len(inpt[0]) and inpt[i - 1][j + 1] == '#':
            return False

    if j - 1 > 0 and inpt[i][j - 1] == '#':
        return False
    if j + 1 < len(inpt[0]) and inpt[i][j + 1] == '#':
        return False

    if i + 1 < len(inpt):
        if j - 1 > 0 and inpt[i + 1][j - 1] == '#':
            return False
        if inpt[i + 1][j] == '#':
            return False
        if j + 1 < len(inpt[0]) and inpt[i + 1][j + 1] == '#':
            return False
    return True


def main():
    with open('11test.txt') as f:
        print(solution(parse(f.read())))


main()

def parse(f):
    return [list(line) for line in f.strip().split('\n')]


def solution(inpt):
    changed = True
    new_inpt = [['' for i in range(len(inpt[0]))] for j in range(len(inpt))]
    new_inpt = copy_matrix(inpt, new_inpt)
    rounds = 0
    while changed:
        rounds += 1
        changed = do_round(inpt, new_inpt)
        inpt = copy_matrix(new_inpt, inpt)
    return count_occupied(new_inpt)


def count_occupied(inpt):
    count = 0
    for line in inpt:
        for elem in line:
            count += 1 if elem == '#' else 0
    return count


def copy_matrix(source, dest):
    for i in range(len(dest)):
        for j in range(len(dest[0])):
            dest[i][j] = source[i][j]
    return dest


def do_round(inpt, new_inpt):
    changed = False
    for i in range(len(inpt)):
        for j in range(len(inpt[i])):
            if step(i, j, inpt, new_inpt):
                changed = True
    return changed


def step(i, j, inpt, new_inpt):
    n = count_occupied_neighbours(i, j, inpt)
    if inpt[i][j] == 'L' and n == 0:
        new_inpt[i][j] = '#'
        return True

    if inpt[i][j] == '#' and n >= 5:
        new_inpt[i][j] = 'L'
        return True
    return False


def count_occupied_neighbours(i, j, inpt):
    count = 0
    k = 1
    while i - k >= 0:
        if inpt[i - k][j] == 'L':
            break
        if inpt[i - k][j] == '#':
            count += 1
            break
        k += 1

    k = 1
    while i - k >= 0 and j + k < len(inpt[0]):
        if inpt[i - k][j + k] == 'L':
            break
        if inpt[i - k][j + k] == '#':
            count += 1
            break
        k += 1

    k = 1
    while j + k < len(inpt[0]):
        if inpt[i][j + k] == 'L':
            break
        if inpt[i][j + k] == '#':
            count += 1
            break
        k += 1

    k = 1
    while i + k < len(inpt) and j + k < len(inpt[0]):
        if inpt[i + k][j + k] == 'L':
            break
        if inpt[i + k][j + k] == '#':
            count += 1
            break
        k += 1

    k = 1
    while i + k < len(inpt):
        if inpt[i + k][j] == 'L':
            break
        if inpt[i + k][j] == '#':
            count += 1
            break
        k += 1

    k = 1
    while i + k < len(inpt) and j - k >= 0:
        if inpt[i + k][j - k] == 'L':
            break
        if inpt[i + k][j - k] == '#':
            count += 1
            break
        k += 1

    k = 1
    while j - k >= 0:
        if inpt[i][j - k] == 'L':
            break
        if inpt[i][j - k] == '#':
            count += 1
            break
        k += 1

    k = 1
    while i - k >= 0 and j - k >= 0:
        if inpt[i - k][j - k] == 'L':
            break
        if inpt[i - k][j - k] == '#':
            count += 1
            break
        k += 1

    return count


def check(i, j, k, inpt):
    if inpt[i - k][j] == 'L':
        return False
    if inpt[i - k][j] == '#':
        return True


def main():
    with open('11test.txt') as f:
        print(solution(parse(f.read())))


main()

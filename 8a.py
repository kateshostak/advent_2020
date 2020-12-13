def parse(f):
    d = []
    for line in f.strip().split('\n'):
        instr, arg = line.split(' ')
        d.append([instr, arg[0], arg[1:]])
    return d


def solution(inpt):
    times_executed = [0]*len(inpt)
    sum_ = 0
    pos = 0
    while True:
        instr, sign, arg = inpt[pos]
        times_executed[pos] += 1
        if times_executed[pos] > 1:
            return sum_

        if instr == 'acc':
            sum_ = acc(sum_, sign, int(arg))
            pos += 1
            continue
        elif instr == 'jmp':
            pos = jmp(pos, sign, int(arg))
            continue
        elif instr == 'nop':
            pos += 1
            continue


def acc(var, sign, arg):
    if sign == '+':
        return var + arg
    return var - arg


def jmp(pos, sign, offset):
    if sign == '+':
        return pos + offset
    return pos - offset


def main():
    with open('8.txt') as f:
        print(solution(parse(f.read())))


main()

def parse(f):
    d = []
    for line in f.strip().split('\n'):
        instr, arg = line.split(' ')
        d.append([instr, arg[0], arg[1:]])
    return d


def solution(inpt):
    prev = ''
    print(len(inpt))
    for i in range(len(inpt)):
        if inpt[i][0] == 'jmp':
            prev = 'jmp'
            inpt[i][0] = 'nop'
        elif inpt[i][0] == 'nop':
            prev = 'nop'
            inpt[i][0] = 'jmp'

        ans = run(inpt)
        if ans == 'loop':
            if inpt[i][0] != 'acc':
                inpt[i][0] = prev
        else:
            print(i, prev, inpt[i][0])
            return ans


def run(inpt):
    pos = 0
    sum_ = 0
    times_executed = [0]*len(inpt)
    while True:
        if pos == len(inpt):
            return sum_
        instr, sign, arg = inpt[pos]
        times_executed[pos] += 1
        if times_executed[pos] > 1:
            return 'loop'
        if instr == 'acc':
            sum_ = acc(sum_, sign, int(arg))
        elif instr == 'jmp':
            pos = jmp(pos, sign, int(arg))
            continue
        pos += 1


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

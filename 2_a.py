def valid_pass_count(path):
    res = 0
    with open(path) as f:
        for line in f:
            edges, letter, word = line.split(' ')
            low, high = map(int, edges.split('-'))
            n = word.count(letter.strip(':'))
            if n >= low and n <= high:
                res += 1

    return res


def main():
    print(valid_pass_count('2_a.txt'))


if __name__ == '__main__':
    main()

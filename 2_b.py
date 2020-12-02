def valid_pass_count(path):
    res = 0
    with open(path) as f:
        for line in f:
            edges, letter, word = line.split(' ')
            letter = letter.strip(':')
            low, high = map(int, edges.split('-'))
            if word[low - 1] == letter and word[high - 1] == letter:
                continue
            if word[low - 1] != letter and word[high - 1] != letter:
                continue
            res += 1

    return res


def main():
    print(valid_pass_count('2_a.txt'))


if __name__ == '__main__':
    main()

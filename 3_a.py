def count_trees(map_):
    trees = 0
    k = 0
    for i in range(1, len(map_)):
        k += 3
        k %= len(map_[0]) - 1
        if map_[i][k] == '#':
            trees += 1

    return trees


def main():
    map_ = []
    with open('3_a.txt') as f:
        for line in f:
            map_.append(line)

    print(count_trees(map_))


if __name__ == '__main__':
    main()

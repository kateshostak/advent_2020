def count_trees(map_):
    res = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for right, down in slopes:
        i = 0
        j = 0
        trees = 0
        while i < len(map_) - down:
            i += down
            j += right
            j %= len(map_[0]) - 1
            if map_[i][j] == '#':
                trees += 1
        res *= trees

    return res


def main():
    map_ = []
    with open('3_a.txt') as f:
        for line in f:
            map_.append(line)

    print(count_trees(map_))


if __name__ == '__main__':
    main()

def sum2020(arr):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while i != j:
        if arr[i] + arr[j] == 2020:
            return arr[i] * arr[j]
        if arr[i] + arr[j] > 2020:
            j -= 1
        else:
            i += 1


def main():
    arr = []
    with open('1_a.txt') as f:
        for line in f:
            arr.append(int(line))
    print(sum2020(arr))


if __name__ == '__main__':
    main()

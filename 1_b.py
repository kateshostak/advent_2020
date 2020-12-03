def sum3_2020(arr):
    arr.sort()
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 1):
            q = j
            k = len(arr) - 1
            while k != q:
                if arr[i] + arr[q] + arr[k] == 2020:
                    return arr[i] * arr[q] * arr[k]
                if 2020 - arr[i] - arr[q] < arr[k]:
                    k -= 1
                else:
                    q += 1


def main():
    arr = []
    with open('1_a.txt') as f:
        for line in f:
            arr.append(int(line))

    print(sum3_2020(arr))


if __name__ == '__main__':
    main()

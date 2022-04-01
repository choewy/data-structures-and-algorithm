from sys import stdin

input = stdin.readline


# 집합 풀이
def solution1() -> None:
    ##### TEST #####
    # M, N = 5, 3
    # items, targets = {2, 3, 7, 8, 9}, [5, 7, 9]
    ################

    N = int(input())
    items = set(map(int, input().rstrip().split()))
    M = int(input())
    targets = list(map(int, input().rstrip().split()))

    res = []
    for target in targets:
        res.append('yes' if target in items else 'no')

    print(' '.join(res))


# 이진 탐색
def solution2() -> None:
    def binarySearch(arr, value, start, end) -> str:
        if start > end:
            return 'no'

        mid = (start + end) // 2

        if arr[mid] == value:
            return 'yes'

        if arr[mid] < value:
            return binarySearch(arr, value, mid+1, end)
        else:
            return binarySearch(arr, value, start, mid-1)

    ##### TEST #####
    # M, N = 5, 3
    # items, targets = [2, 3, 7, 8, 9], [5, 7, 9]
    ################

    N = int(input())
    items = sorted(list(map(int, input().rstrip().split())))
    M = int(input())
    targets = list(map(int, input().rstrip().split()))

    res = []
    for target in targets:
        res.append(binarySearch(items, target, 0, len(items)-1))

    print(' '.join(res))

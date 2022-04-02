for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    max_distance = 0
    count = 0
    flag = False
    increase = 1

    while distance > max_distance:
        max_distance += increase
        count += 1

        if flag:
            increase += 1

        flag = not(flag)

    print(count)

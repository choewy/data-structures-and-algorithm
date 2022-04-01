for _ in range(int(input())):
    k, n = map(int, [input(), input()])

    rooms = [[i+1 for i in range(n)]]

    for i in range(k):
        rooms.append([sum(rooms[i][:j+1]) for j in range(n)])

    print(rooms[k][n-1])

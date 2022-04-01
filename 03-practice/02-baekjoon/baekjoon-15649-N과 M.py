def recursive(num):
    if num == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            res.append(i)
            recursive(num + 1)
            visited[i] = False
            res.pop()


N, M = map(int, input().split())
res, visited = [], [False]*(N+1)
recursive(0)

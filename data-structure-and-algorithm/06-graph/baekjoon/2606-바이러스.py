cnt = int(input())

if cnt == 0:
    print(0)

else:
    pares = [[] for _ in range(cnt)]

    for _ in range(int(input())):
        fc, tc = map(int, input().split())

        # 양방향으로 수정
        pares[fc-1].append(tc-1)
        pares[tc-1].append(fc-1)

    def recursive(index):
        if visited[index] == 1:
            return

        visited[index] = 1

        for c in pares[index]:
            recursive(c)

    visited = [0]*len(pares)
    current = 0
    recursive(current)
    print(sum(visited) - 1)

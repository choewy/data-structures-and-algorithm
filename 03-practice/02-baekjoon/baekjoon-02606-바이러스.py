# =========== 1차 시도 ============
# PARES = {c+1: [] for c in range(int(input()))}
#
# for _ in range(int(input())):
#     computer, link = map(int, input().split())
#     PARES[computer].append(link)
#
# visited = []
# computers = PARES[1]
#
#
# def recursive(cps):
#     for cp in cps:
#         if cp in visited:
#             continue
#         visited.append(cp)
#         recursive(PARES[cp])
#
#
# recursive(computers)
# print(len(visited))

# =========== 2차 시도 ============
# cnt = int(input())
#
# if cnt == 0:
#     print(0)
#
# else:
#     pares = [[]] + [[] for _ in range(cnt)]
#
#     for _ in range(int(input())):
#         fc, tc = map(int, input().split())
#         pares[fc].append(tc)
#
#
#     def recursive(cps):
#         for cp in cps:
#             if cp in visited:
#                 continue
#             visited.append(cp)
#             recursive(pares[cp])
#
#
#     visited = []
#     recursive(pares[1])
#     # visited.remove(1)
#     print(pares)
#     print(visited)
#     print(len(visited))

# ======= 3차 시도 =========

cnt = int(input())

if cnt == 0:
    print(0)

else:
    pares = [[] for _ in range(cnt)]

    for _ in range(int(input())):
        fc, tc = map(int, input().split())
        # 양방향으로 해야됨
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


"""
input values

7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

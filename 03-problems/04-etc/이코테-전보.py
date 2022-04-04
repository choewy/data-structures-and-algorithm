import heapq
from typing import List
from sys import stdin

INF = int(1e9)
input = stdin.readline


def solution(nmc: List[int] = None, xyz: List[List[int]] = None) -> None:
    n, m, c = nmc if nmc else map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF]*(n + 1)

    for i in range(m):
        x, y, z = xyz[i] if xyz else map(int, input().rstrip().split())
        graph[x].append((y, z))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(c)

    count = 0
    max_dist = 0
    for dist in distance:
        if dist != INF:
            count += 1
            max_dist = max(max_dist, dist)

    print(count-1, max_dist)


if __name__ == "__main__":
    cases = [
        [
            [3, 2, 1],
            [
                (1, 2, 4),
                (1, 3, 2)
            ]
        ]
    ]

    for case in cases:
        nmc, xyz = case
        solution(nmc, xyz)

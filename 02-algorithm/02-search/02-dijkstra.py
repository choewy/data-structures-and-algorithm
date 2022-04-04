import heapq
from typing import List, Tuple
from sys import stdin

input = stdin.readline


# 그리디 알고리즘에 포함
# 간단한 다익스트라 알고리즘 : O(N^2)
def simpleSolution(
    nm: List[int] = None,
    start: int = None,
    graph: List[List[Tuple[int]]] = None
) -> None:

    INF = int(1e9)
    n, m = nm if nm else map(int, input().rstrip().split())
    start = start if start else int(input().rstrip())

    if not graph:
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, input().rstrip().split())
            graph[a].append((b, c))

    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # 이 부분을 heapq로 구현하면?
    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now] + j[1]

                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print('INFINITY')
        else:
            print(distance[i])


# 다이나믹 프로그래밍에 포함
# 개선된 다익스트라 알고리즘 : O(ElogV)
# (V: 노드의 개수, E 간선의 개수)
def improvedSolution(
    nm: List[int] = None,
    start: int = None,
    graph: List[List[Tuple[int]]] = None
) -> None:

    INF = int(1e9)
    n, m = nm if nm else map(int, input().rstrip().split())
    start = start if start else int(input().rstrip())

    if not graph:
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, c = map(int, input().rstrip().split())
            graph[a].append((b, c))

    distance = [INF] * (n + 1)

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

    dijkstra(start)

    for i in range(1, n+1):
        if distance[i] == INF:
            print('INFINITY')
        else:
            print(distance[i])


# 기존 (노드번호, 거리) 순의 튜플을
# (거리, 노드번호)순으로 바꾼 후
# 우선순위큐에 삽입
"""
init:
    heapq: [(0, 1)]
node: (0, 1)
    heapq: [(1, 4), (2, 2), (5, 3)]
node: (1, 4)
    heapq: [(2, 2), (2, 5), (4, 3), (5, 3)]
node: (2, 2)
    heapq: [(2, 5), (4, 3), (5, 3)]
node: (2, 5)
    heapq: [(3, 3), (4, 3), (4, 6), (5, 3)]
node: (3, 3)
    heapq: [(4, 3), (4, 6), (5, 3)]
node: (4, 3)
    heapq: [(4, 6), (5, 3)]
node: (4, 6)
    heapq: [(5, 3)]
node: (5, 3)
    heapq: []
"""


# 테스트
if __name__ == "__main__":
    cases = [
        [
            [6, 11],
            1,
            [
                [],
                [(2, 2), (3, 5), (4, 1)],
                [(3, 3), (4, 2)],
                [(2, 3), (6, 5)],
                [(3, 3), (5, 1)],
                [(3, 1), (6, 2)],
                []
            ]
        ]
    ]

    for case in cases:
        nm, start, graph = case
        improvedSolution(nm, start, graph)

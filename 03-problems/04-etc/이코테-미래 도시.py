# <문제>
"""
1번 회사에서 K번 회사를 들려, X번 회사까지로 가는 최단거리를 구하라.
(단, 모든 간선의 비용은 1이며, 양방향이다.)
(만약, X번 회사까지 도달할 수 없다면 -1을 반환한다.)
"""

# <입력>
"""
첫째 줄 : 전체 회사의 개수 N(1 ≤ N ≤ 100), 간선의 개수 M(1 ≤ M ≤ 100)
둘째 줄 ~ M + 1째 줄 : 두 회사의 연결 정보
M + 2째 줄 : X와 K(1 ≤ K ≤ 100)
"""


from typing import List
from sys import stdin
input = stdin.readline


def solution(
    nm: List[int] = None,
    ab: List[List[int]] = None,
    xk: List[int] = None
) -> None:

    INF = int(1e9)

    n, m = nm if nm else map(int, input().rstrip().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for i in range(m):
        a, b = ab[i] if ab else map(int, input().rstrip().split())
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = xk if xk else map(int, input().rstrip().split())

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    distance = graph[1][k] + graph[k][x]
    print(-1 if distance == INF else distance)


if __name__ == "__main__":
    cases = [
        [
            [5, 7],
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 4],
                [3, 4],
                [3, 5],
                [4, 5]
            ],
            [4, 5]
        ]
    ]

    for case in cases:
        nm, ab, xk = case
        solution(nm, ab, xk)

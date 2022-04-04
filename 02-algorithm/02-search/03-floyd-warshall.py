# 모든 노드에서 다른 노드까지의 최단 경로 계산
# 다익스트라와 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
# 단, 매 단계마다 방문하지 않은 노드 중 최단 거리를 갖는 노드를 찾지 않아도 됨
# 2차원 테이블에 최단 거리 정보를 저장
# 다이다믹 프로그래밍에 포함

from typing import List


# 시간 복잡도 : O(N^3)
# 따라서, 노드의 개수가 500개 이하인 경우에 사용
def solution(nm: List[int] = None, abc: List[List[int]] = None) -> None:
    INF = int(1e9)
    n, m = nm if nm else map(int, input().rstrip().split())
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for x in range(1, n+1):
        graph[x][x] = 0

    abc = abc if abc else [
        list(map(int, input().rstrip().split())) for _ in range(m)
    ]

    for a, b, c in abc:
        graph[a][b] = c

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                ab = graph[a][b]
                ak_kb = graph[a][k] + graph[k][b]
                graph[a][b] = min(ab, ak_kb)

    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()


if __name__ == "__main__":
    cases = [
        [
            [4, 7],
            [
                [1, 2, 4],
                [1, 4, 6],
                [2, 1, 3],
                [2, 3, 7],
                [3, 1, 5],
                [3, 4, 4],
                [4, 3, 2],
            ]
        ],
    ]

    for case in cases:
        nm, abc = case
        solution(nm, abc)

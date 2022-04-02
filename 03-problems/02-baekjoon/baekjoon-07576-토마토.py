from typing import List
from sys import stdin
input = stdin.readline


def solution(mn: List[int] = None, box: List[int] = None) -> int:
    m, n = mn if mn else map(int, input().rstrip().split())
    box = box if box else [
        list(map(int, input().rstrip().split())) for _ in range(n)]

    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]

    q, rc = [], []
    for row in range(n):
        for col in range(m):
            if box[row][col] == 1:
                rc.append((row, col))
    q.append(rc)

    cnt = 0
    while q:
        rc = q[0]
        q = q[1:]

        nrc = []
        for r, c in rc:
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m or box[nr][nc] != 0:
                    continue
                box[nr][nc] = 1
                if (nr, nc) not in q:
                    nrc.append((nr, nc))
        if nrc:
            cnt += 1
            q.append(nrc)

    for row in box:
        if row.count(0):
            return -1

    return cnt


if __name__ == "__main__":
    mode = 'test'

    if mode == 'test':
        cases = [
            [
                [6, 4],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1]
                ]
            ],
            [
                [6, 4],
                [
                    [0, -1, 0, 0, 0, 0],
                    [-1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1]
                ]
            ],
            [
                [6, 4],
                [
                    [1, -1, 0, 0, 0, 0],
                    [0, -1, 0, 0, 0, 0],
                    [0, 0, 0, 0, -1, 0],
                    [0, 0, 0, 0, -1, 1]
                ]
            ],
            [
                [5, 5],
                [
                    [-1, 1, 0, 0, 0],
                    [0, -1, -1, -1, 0],
                    [0, -1, -1, -1, 0],
                    [0, -1, -1, -1, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            [
                [2, 2],
                [
                    [1, -1],
                    [-1, 1],
                ]
            ]
        ]

        outputs = [
            8,
            -1,
            6,
            14,
            0
        ]

        for case, output in zip(cases, outputs):
            mn, box = case
            print(solution(mn, box))
    else:
        print(solution())


"""
1) 입력받은 배열에서 1인 좌표를 모두 찾아내서 임시 배열에 추가
2) 임시배열에 담긴 모든 좌표를 큐에 넣고 bfs 탐색
"""

"""
day = 0
0 0 0 0 0 0     
0 0 0 0 0 0     
0 0 0 0 0 0     
0 0 0 0 0 1     

day = 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 1 1

day = 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 1 1
0 0 0 1 1 1

day = 3
0 0 0 0 0 1
0 0 0 0 1 1
0 0 0 1 1 1
0 0 1 1 1 1

day = 4
0 0 0 0 1 1
0 0 0 1 1 1
0 0 1 1 1 1
0 1 1 1 1 1

day = 5
0 0 0 1 1 1
0 0 1 1 1 1
0 1 1 1 1 1
1 1 1 1 1 1

day = 6
0 0 1 1 1 1
0 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1

day = 7
0 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1

day = 8
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
"""

"""
day = 0
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

day = 1
1 -1 0 0 0 0
1 -1 0 0 0 0
0 0 0 0 -1 1
0 0 0 0 -1 1

day = 2
1 -1 0 0 0 0
1 -1 0 0 0 1
1 0 0 0 -1 1
0 0 0 0 -1 1

day = 3
1 -1 0 0 0 1
1 -1 0 0 1 1
1 1 0 0 -1 1
1 0 0 0 -1 1

day = 4
1 -1 0 0 1 1
1 -1 0 1 1 1
1 1 1 0 -1 1
1 1 0 0 -1 1

day = 5
1 -1 0 1 1 1
1 -1 1 1 1 1
1 1 1 1 -1 1
1 1 1 0 -1 1

day = 6
1 -1 1 1 1 1
1 -1 1 1 1 1
1 1 1 1 -1 1
1 1 1 1 -1 1
"""

# <문제>
"""
최소 힙을 이용하여 다음과 같은 연산을 수행하라.
1) 배열에 자연수 x 추가.
2) 배열에서 가장 작은 값을 출력, 그 값을 배열에서 출력.
"""

# <입력>
"""
1) 첫 번째 줄: X의 개수 N(1 ≤ N ≤ 100,000)
2) 두 번째 ~ N + 1번째 줄: 연산에 대한 정보를 나타내는 정수 X(0 ≤ x < 2^31)
"""

# <조건>
"""
1) x가 자연수: 배열에 X 추가.
2) x가 0: 배열에서 가장 작은 값 출력 및 해당 값을 배열에서 제거.
3) 입력에서 0이 주어진 만큼 답을 출력.
4) 배열이 비어있을 경우 0을 출력.
"""

# <제출코드>
from sys import stdin
input = stdin.readline


class BinaryMinHeap:
    def __init__(self) -> None:
        self.items = [None]

    def __len__(self) -> int:
        return len(self.items) - 1

    def _percolate_up(self) -> None:
        cr = len(self)
        pr = cr // 2

        while pr > 0:
            if self.items[cr] < self.items[pr]:
                self.items[cr], self.items[pr] = self.items[pr], self.items[cr]

            cr, pr = pr, cr // 2

    def insert(self, val: int) -> None:
        self.items.append(val)
        self._percolate_up()

    def _percolate_down(self, cr) -> None:
        sm, le, ri = cr, cr*2, cr*2+1

        if le <= len(self) and self.items[le] < self.items[sm]:
            sm = le

        if ri <= len(self) and self.items[ri] < self.items[sm]:
            sm = ri

        if sm != cr:
            self.items[cr], self.items[sm] = self.items[sm], self.items[cr]
            self._percolate_down(sm)

    def extract(self) -> int:
        if len(self) < 1:
            return 0

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def solution(N: int = None, X: int = None) -> int:
    N = int(input()) if N is None else N
    X = [int(input()) for _ in range(N)] if X is None else X

    heap = BinaryMinHeap()

    for x in X:
        if x == 0:
            print(0 if len(heap) == 0 else heap.extract())
            continue

        heap.insert(x)


# <테스트>
if __name__ == "__main__":
    testcases = [
        [9, [0, 12345678, 1, 2, 0, 0, 0, 0, 32]]
    ]
    for case in testcases:
        N, X = case
        solution(N, X)

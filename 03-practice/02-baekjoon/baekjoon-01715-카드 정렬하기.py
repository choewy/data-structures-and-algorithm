import heapq
from sys import stdin

input = stdin.readline

"""
# 주어진 원소의 개수가 N개 일때, 시간 복잡도는 O(N^2 * logN)
# N = 100,000일때, 시간 복잡도 1억 초과(기본 5초 이상 소요됨 -> 문제에서는 2초 이내 제한 있음)
# 참고로, 파이썬은 1초에 약 20,000,000 번 연산이 가능하다고 한다.
def solution() -> None:
    n = int(input())
    if n == 1:
        print(0)
    else:
        total = 0
        cards = sorted([int(input()) for _ in range(n)], reverse=True)
        while len(cards) > 1:
            card1 = cards.pop()
            card2 = cards.pop()
            cnt = card1 + card2
            cards.append(cnt)
            total += cnt
        print(total)
"""


def solution() -> None:
    n = int(input())
    if n == 1:
        print(0)

    else:
        total = 0
        cards = [int(input()) for _ in range(n)]
        heapq.heapify(cards)

        while len(cards) > 1:
            card1 = heapq.heappop(cards)
            card2 = heapq.heappop(cards)
            next = card1 + card2
            heapq.heappush(cards, next)
            total += next

        print(total)


solution()

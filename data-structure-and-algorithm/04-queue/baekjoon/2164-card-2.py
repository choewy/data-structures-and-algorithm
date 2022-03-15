from collections import deque

N = int(input())

cards = deque([n for n in range(1, N+1)])

while cards.__len__() > 1:
    cards.popleft()
    n = cards.popleft()
    cards.append(n)

print(cards.pop())

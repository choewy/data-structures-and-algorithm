import sys

for (a, b) in [list(map(int, sys.stdin.readline().rstrip().split(' ')))
               for _ in range(int(sys.stdin.readline().rstrip()))]:
    print(a + b)

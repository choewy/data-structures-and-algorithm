n, x = map(int, input().split(' '))
print(' '.join(map(str, list(filter(lambda v: v < x, list(map(int, input().split(' '))))))))

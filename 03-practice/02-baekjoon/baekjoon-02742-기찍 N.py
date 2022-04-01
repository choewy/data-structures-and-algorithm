import sys
lst = [f'{n+1}' for n in range(int(sys.stdin.readline().rstrip()))]
lst.reverse()
print('\n'.join(lst))

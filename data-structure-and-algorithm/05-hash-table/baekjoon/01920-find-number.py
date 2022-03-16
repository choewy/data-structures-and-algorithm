input()
A = set(input().split())

input()
M = input().split()

print('\n'.join(["1" if m in A else "0" for m in M]))

a = int(input())
b = [int(n) for n in input()]
b.reverse()

t = 0

for i, n in enumerate(b):
    t += (a * n) * (10 ** i)
    print(a * n)

print(t)

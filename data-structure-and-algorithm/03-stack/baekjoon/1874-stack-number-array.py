num = 0
stack = []
res = []
correct = True

for i in range(int(input())):
    n = int(input())

    while num < n:
        num += 1
        stack.append(num)
        res.append("+")

    if stack[-1] == n:
        stack.pop()
        res.append("-")
    else:
        correct = False
        break

if not correct:
    print("NO")
else:
    print("\n".join(res))

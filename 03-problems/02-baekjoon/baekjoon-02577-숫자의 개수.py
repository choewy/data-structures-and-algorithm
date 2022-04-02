a = int(input())
b = int(input())
c = int(input())
v = str(a * b * c)

for i in range(10):
    print(v.count(f'{i}'))

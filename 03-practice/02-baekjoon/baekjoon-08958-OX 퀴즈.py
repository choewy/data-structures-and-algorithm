def sum_(value):
    return value*(value+1)//2


for result in [input().split('X') for _ in range(int(input()))]:
    if '' in result:
        result.remove('')

    print(sum([sum_(len(r)) for r in result]))

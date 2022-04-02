n = int(input())
cnt = 0

if n < 100:
    cnt += n

else:
    cnt += 99
    for i in range(100, n+1):
        lst = list(map(int, str(i)))
        if lst[2] == lst[1] + lst[1] - lst[0]:
            cnt += 1

print(cnt)

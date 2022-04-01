# https://www.acmicpc.net/problem/1759
# 재시도 필요

L, C = map(int, input().split())
# L, C = 4, 6

vowels = ['a', 'e', 'i', 'o']
alphabets = input().split()
# alphabets = ['a', 'c', 'i', 's', 't', 'w']
alphabets.sort()
passwds = []


def recursive(idx, arr):
    if len(arr) == L:
        passwds.append(''.join(arr))
        return

    for i in range(idx, C):
        alphabet = alphabets[i]
        recursive(i+1, arr+[alphabet])


recursive(0, [])

for passwd in passwds:
    vp = 0
    cp = 0
    for alphabet in passwd:
        if alphabet in vowels:
            vp += 1
        else:
            cp += 1

    if vp < 1 or cp < 2:
        continue

    print(passwd)

N, M = map(int, input().split())

hashtable = {}
for _ in range(N):
    site, passwd = input().split()
    hashtable[site] = passwd

for _ in range(M):
    site = input()
    print(hashtable[site])

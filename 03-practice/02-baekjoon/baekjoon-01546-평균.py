n = int(input())
scores = list(map(int, input().split(' ')))
m = max(scores)

for i, score in enumerate(scores):
    scores[i] = score/m*100

print(sum(scores)/n)

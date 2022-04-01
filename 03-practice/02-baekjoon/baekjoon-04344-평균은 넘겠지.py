for _ in range(int(input())):
    scores = list(map(int, input().split(' ')))
    cnt = scores.pop(0)
    print('%.3f%%' % round(
        len(list(filter(lambda score: score > sum(scores)/cnt, scores)))/cnt*100, 3))

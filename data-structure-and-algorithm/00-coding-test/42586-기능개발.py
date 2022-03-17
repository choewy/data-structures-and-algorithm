from math import ceil


def solution(progresses, speeds):
    counts = []

    days = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    days.reverse()

    while days:
        cnt = 1
        current = days.pop()
        while days:
            day = days.pop()
            if day > current:
                days.append(day)
                break
            cnt += 1
        counts.append(cnt)
    return counts


solution([93, 30, 55], [1, 30, 5])

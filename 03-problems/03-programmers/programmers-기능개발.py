def solution(progresses: list, speeds: list) -> list:
    counts = []

    days = [((100-p)//s)+1 if (100-p)/s > (100-p)//s else (100-p)//s
            for p, s in zip(progresses, speeds)]
    days.reverse()

    while days:
        cnt = 1
        current = days.pop()

        while days:
            next = days.pop()
            if next > current:
                days.append(next)
                break

            cnt += 1
        counts.append(cnt)
    return counts

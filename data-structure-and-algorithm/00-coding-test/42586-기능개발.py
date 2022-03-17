def solution(progresses, speeds):
    counts = []

    # 진행률을 기반으로 며칠 소요될 것인지 계산(올림 처리)
    days = [((100-p)//s)+1 if (100-p)/s > (100-p)//s else (100-p)//s
            for p, s in zip(progresses, speeds)]

    # Queue로 사용하기 위하여 역순(내림차순 아님) 정렬
    days.reverse()

    while days:
        # 배포 수 초기화
        cnt = 1

        # 기능 배포 대기
        current = days.pop()

        while days:
            # 다음 기능 배포 대기
            next = days.pop()

            # 다음 기능의 완료일이 이전 기능의 완료일보다 늦는 경우
            if next > current:
                days.append(next)
                break

            # 다음 기능의 완료일이 이전 기능의 완료일보다 빠르거나 같은 경우
            cnt += 1
        counts.append(cnt)
    return counts

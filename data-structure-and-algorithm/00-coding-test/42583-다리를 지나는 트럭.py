def solution(bridge_length: int, bridge_weight: int, trucks: list):
    # Queue로 사용하기 위해 역순(내림차순 아님) 정렬
    trucks.reverse()

    # 소요 시간
    time = 0

    # 다리를 건너고 있는 트럭(예외처리를 위해 0으로 입력함)
    crossed = [0]*bridge_length

    # 현재 다리 위 트럭의 총 무게
    weights = 0

    while trucks:
        # 시간 증가 및 현재 다리 위 트럭 1개 제거(건넌 상태)
        time += 1
        weights -= crossed.pop()

        # 다리 위에 트럭 한 대가 더 올라가도 버틸 수 있는지?
        if trucks[-1] + weights <= bridge_weight:
            # 다리 위에 트럭 추가(Queue로 사용하기 위해 역순 정렬)
            crossed = [trucks.pop()] + crossed
            weights += crossed[0]
        else:
            # Queue로 사용하기 위해 역순 정렬
            crossed = [0] + crossed

    # 총 소요 시간 = 소요 시간 + 다리 길이
    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))

def solution(bridge_length: int, bridge_weight: int, trucks: list) -> int:
    trucks.reverse()

    time = 0
    crossed = [0]*bridge_length
    weights = 0

    while trucks:
        time += 1
        weights -= crossed.pop()

        if trucks[-1] + weights <= bridge_weight:
            crossed = [trucks.pop()] + crossed
            weights += crossed[0]
        else:
            crossed = [0] + crossed

    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))

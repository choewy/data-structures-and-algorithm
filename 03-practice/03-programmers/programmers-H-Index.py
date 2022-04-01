def solution(citations):
    # [3, 0, 6, 1, 5]에서
    # 3(arr[0])번 이상 인용된 논문: 3편 이상(3, 6, 5) => h = 3
    # 0(arr[1])번 이상 인용된 논문 => 해당없음
    # 6(arr[2])번 이상 인용된 논문: 6편 이하(6) => 해당없음
    # 1(arr[3])번 이상 인용된 논문: 1편 이상(3, 6, 1, 5) => h = 1
    # 5(arr[4])번 이상 인용된 논문: 5편 이하(5, 6) => 해당없음
    # 즉, 해당 수보다 높은 수의 개수를 먼저 파악하고
    answer = 0
    citations.sort()
    for seq in range(1, len(citations) + 1):
        count = len(list(filter(lambda x: seq <= x, citations)))
        print(seq, count)
        if seq > count:
            print('return', seq, count)
            return seq - 1
        else:
            answer = seq
    print()
    return answer


if __name__ == "__main__":
    cases = [[3, 0, 6, 1, 5], [6, 6, 6, 6, 6, 1], [4, 0], []]
    output = [3, 5]
    for case in cases:
        print(solution(case))


# <문제 설명>
"""
n개의 음이 아닌 정수들이 있습니다.
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

1) -1+1+1+1+1 = 3
2) +1-1+1+1+1 = 3
3) +1+1-1+1+1 = 3
4) +1+1+1-1+1 = 3
5) +1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
"""

# <제한사항>
"""
1) 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
2) 각 숫자는 1 이상 50 이하인 자연수입니다.
3) 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""


def solution(numbers, target) -> int:
    length = len(numbers)

    def recursive(index, total) -> None:
        if index >= length:
            if total == target:
                nonlocal answer
                answer += 1
            return
        else:
            recursive(index + 1, total + numbers[index])
            recursive(index + 1, total - numbers[index])

    answer = 0
    recursive(0, 0)

    return answer


if __name__ == "__main__":
    print(solution([4, 1, 2, 1], 4) == 2)


# <로직>
"""
index 1씩 늘려가면서 +경우와 -경우로 나누어 재귀호출
예) 
- [index 0: 4]: 4로 출발하는 경우와 -4로 출발하는 경우로 나누어 재귀호출
    - [index 1: 1]: 4에 +1하는 경우와 -1하는 경우로 나누어 재귀호출
        - [index 2: 2]: ...
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
        - [index 2: 2]: ...
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
    - [index 1: 1]: -4에 +1하는 경우와 -1하는 경우로 나누어 재귀호출
        - [index 2: 2]: ...
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
        - [index 2: 2]: ...
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return
            - [index3: 1]: ...
                - [index4: OutofIndex]: total == target && answer += 1 -> return
                - [index4: OutofIndex]: total == target && answer += 1 -> return

"""

# <로직 상세>
# TEST CASE : numbers = [4, 1, 2, 1], target = 4
"""
(0, 0) 
-> (1, 0 + 4): 4
    -> (2, 4 + 1): 5
        -> (3, 5 + 2): 7
            -> (4, 7 + 1): 8 -> return
            -> (4, 7 - 1): 6 -> return
        -> (3, 5 - 2): 3
            -> (4, 3 + 1): 4 -> answer += 1 -> return
            -> (4, 3 - 1): 2 -> return
    -> (2, 4 - 1): 3
        -> (3, 3 + 2: 5
            -> (4, 5 + 1): 6 -> return
            -> (4, 5 - 1): 4 -> answer += 1 -> return
        -> (3, 3 - 2): 1
            -> (4, 1 + 1): 2 -> return
            -> (4, 1 - 1): 0 -> return
-> (1, 0 - 4): -4
    -> (2, -4 + 1): -3
        -> (3, -3 + 2): -1
            -> (4, -1 + 1): 0 -> return
            -> (4, -1 - 1): -2 -> return
        -> (3, -3 - 2): -5
            -> (4, -5 + 1): -4 -> return
            -> (4, -5 - 1): -6 -> return
    -> (2, -4 - 1): -5
        -> (3, -5 + 1): -4
            -> (4, -4 + 1): -3 -> return
            -> (4, -4 - 1): -5 -> return
        -> (3, -5 - 1): -6
            -> (4, -6 + 1): -5 -> return
            -> (4, -6 - 1): -7 -> return
"""

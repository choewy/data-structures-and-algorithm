# <문제>
"""
전화번호 목록의 일관성을 파악하라.
한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
- 예) 선영(91 12 54 26)으로 전화를 걸 때 긴급전화(911)로 걸어짐
"""

# <입력>
"""
1) 첫 째줄 : 테스트케이스의 개수 (1 ≤ t ≤ 50)
2) 둘 째줄 : 전화번호의 수 (1 ≤ n ≤ 10000)
3) 셋 째줄 ~ n + 1줄 : 고유한 전화번호 (1 ≤ p.length ≤ 10)
"""

# <출력>
"""
일관성이 있는 경우 "YES", 없는 경우 "NO"
"""

from sys import stdin
input = stdin.readline


def solution():
    n = int(input())
    nums = sorted([input().rstrip() for _ in range(n)], reverse=True)
    for _ in range(n-1):
        num, next = nums.pop(), nums[-1]
        if next.startswith(num):
            return print("NO")

    print("YES")


for _ in range(int(input())):
    solution()


# <실행과정>
"""
t: 1,
    nums
        => input: ["911", "94625999", "91125426"]
        => sorted: ["97625999", "91125426", "911"]

    loop: 0 <= n < 2,
        n: 0,
            num: "911"
            nums: ["97625999", "91125426"]
            next: "91125426" => ":911:25426" return "NO"


t: 2,
    nums
        => input: ["113", "12340", "123440", "12345", "98346"]
        => sorted: ["98346", "12345", "123440", "12340", "113"]

    loop: 0 <= n < 4,
        => n: 0
            num: "113"
            nums: ["98346", "12345", "123440", "12340"]
            next: "12340" => continue
        
        => n: 1
            num: "12340"
            nums: ["98346", "12345", "123440"]
            next: "123440" => continue
        
        => n: 2
            num: "123440"
            nums: ["98346", "12345"]
            next: "12345" => continue
        
        => n: 3
            num: "12345"
            nums: ["98346"]
            next: "98346" => continue

        => n: 4
            End loop

    return "YES"
"""

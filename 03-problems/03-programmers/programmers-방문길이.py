
# <문제 설명>
"""
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
1) U: 위쪽으로 한 칸
2) D: 아래쪽으로 한 칸
3) R: 오른쪽으로 한 칸
4) L: 왼쪽으로 한 칸

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
좌표평면의 경계는 다음과 같이 이루어져 있습니다.
1) 왼쪽 위(-5, 5)
2) 왼쪽 아래(-5, -5)
3) 오른쪽 위(5, 5)
4) 오른쪽 아래(5, -5)

게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
이때, 좌표평면을 넘어서게 되는 동작은 무시하고 그 다음 동작을 수행합니다.

명령어가 매개변수 dirs로 주어질 때, 
게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
"""

# <제한 사항>
"""
1) dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
2) dirs의 길이는 500 이하의 자연수입니다.
"""


def solution(dirs) -> int:
    dirs = list(dirs)
    dirs.reverse()

    x, y, visit = 0, 0, set()
    while dirs:
        dir = dirs.pop()
        if dir == 'U' and y < 5:
            path = ((x, y), (x, y + 1))
            visit.add(path)
            y += 1

        elif dir == 'D' and y > -5:
            path = ((x, y - 1), (x, y))
            visit.add(path)
            y -= 1

        elif dir == 'R' and x < 5:
            path = ((x, y), (x + 1, y))
            visit.add(path)
            x += 1

        elif dir == 'L' and x > -5:
            path = ((x - 1, y), (x, y))
            visit.add(path)
            x -= 1

    return len(visit)


if __name__ == "__main__":
    print(solution("ULURRDLLU") == 7)
    print(solution("LULLLLLLU") == 7)
    print(solution("UUUDDDLLLLRRRR") == 7)


# <주의 사항>
"""
1) 좌표를 저장하는게 아니라 간선을 저장해야함.
    -> (0, 0)에서 (0, 1)로 이동 시 (0, 1)을 저장하는게 아니라 ((0, 0), (0, 1))을 저장해야함.
2) 간선 저장 시 좌표를 오름차순으로 정렬해야함.
    -> ((0, 1), (1, 1))과 ((1, 1), (0, 1))은 같은데도 불구하고 중복제거가 안 됨
"""

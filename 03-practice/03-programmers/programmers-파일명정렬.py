# 숫자가 시작되는 지점까지가 HEAD
# 숫자가 끝나는 지점까지가 NUMBER
# 나머지가 TAIL

def find_num_start(string):
    i = 0
    for char in string:
        if char.isdigit():
            return i
        i += 1
    return i


def find_num_end(string):
    i = 0
    for char in string:
        if not char.isdigit():
            return i
        i += 1
    return i


def solution(files):
    answer = []
    for file in files:
        num_start_index = find_num_start(file)
        num_end_index = num_start_index + find_num_end(file[num_start_index:])
        head = file[:num_start_index]
        number = file[num_start_index:num_end_index]
        tail = file[num_end_index:]
        answer.append((head, number, tail))
    answer = sorted(answer, key=lambda file: (file[0].upper(), int(file[1])))
    answer = list(map(lambda file: ''.join(file), answer))

    return answer


if __name__ == "__main__":
    cases = [
        ["img12.png", "img10.png", "img02.png",
            "img1.png", "IMG01.GIF", "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress",
            "A-10 Thunderbolt II", "F-14 Tomcat"],
    ]
    outputs = [
        ["img1.png", "IMG01.GIF", "img02.png",
            "img2.JPG", "img10.png", "img12.png"],
        ["A-10 Thunderbolt II", "B-50 Superfortress",
            "F-5 Freedom Fighter", "F-14 Tomcat"],
    ]
    for case, output in zip(cases, outputs):
        print(solution(case) == output)

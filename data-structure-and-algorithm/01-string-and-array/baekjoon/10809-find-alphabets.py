# https://acmicpc.net/problem/10809


from string import ascii_lowercase

word = input()


def solution_1(word: str) -> None:
    output = []

    for alphabet in ascii_lowercase:
        if alphabet in word:
            output.append(str(word.index(alphabet)))
            continue
        output.append("-1")

    print(" ".join(output))


def solution_2(word: str) -> None:
    output = []

    for ascii in range(ord("a"), ord("z")+1):
        alpabet = chr(ascii)
        ok = str(word.index(alpabet)) if alpabet in word else "-1"
        output.append(ok)

    print(" ".join(output))


solution_2("baekjoon")

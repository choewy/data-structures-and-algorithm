count = int(input())
words = [list(input()) for _ in range(count)]
index_listes = [[[i for i, _ in enumerate(
    word) if word[i] == alphabet] for alphabet in set(word)] for word in words]

for index_list in index_listes:
    index_list = list(filter(lambda lst: len(lst) > 1, index_list))
    for lst in index_list:
        length = len(lst)
        if lst[-1] - lst[0] + 1 != length:
            count -= 1
            break

print(count)

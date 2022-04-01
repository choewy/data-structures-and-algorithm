N = int(input())
level = 1

if N > 1:
    max_number = 1

    while N > max_number:
        max_number += 6*(level)
        level += 1

print(level)

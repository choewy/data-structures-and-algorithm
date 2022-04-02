
# for _ in range(int(input())):
#     H, W, N = map(int, input().split())
#     rooms = []

#     for w in range(1, W+1):
#         for h in range(1, H+1):
#             rooms.append(f"{h}{f'0{w}' if w < 10 else w}")

#     print(rooms[N-1])


for _ in range(int(input())):
    H, W, N = map(int, input().split())

    value = [N % H, N//H]

    if value[0]:
        print(f"{value[0]}{'0' if value[1]+1 < 10 else ''}{value[1]+1}")
    else:
        print(f"{H}{'0' if value[1] < 10 else ''}{value[1]}")

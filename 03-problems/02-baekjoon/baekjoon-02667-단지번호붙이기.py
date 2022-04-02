N = int(input())
MAP = [list(input()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
rows = len(MAP)
cols = len(MAP[0])
cnt = 0


def recursive(nx, ny, index):
    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or MAP[nx][ny] == "0":
        return

    MAP[nx][ny] = "0"
    blocks[index] += 1

    for i in range(4):
        recursive(nx + dx[i], ny + dy[i], index)
    return


blocks = []

for row in range(rows):
    for col in range(cols):

        if MAP[row][col] != "1":
            continue

        cnt += 1
        blocks.append(0)
        recursive(row, col, cnt-1)

print(cnt)

blocks.sort()
for block in blocks:
    print(block)

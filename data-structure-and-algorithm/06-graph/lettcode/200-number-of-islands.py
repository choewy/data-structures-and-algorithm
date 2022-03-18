from typing import List


# iterative
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] != "1":
                    continue

                cnt += 1
                stack = [(row, col)]

                while stack:
                    x, y = stack.pop()
                    grid[x][y] = "0"
                    for xx, yy in zip(dx, dy):
                        nx = x + xx
                        ny = y + yy
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != "1":
                            continue
                        stack.append((nx, ny))
        return cnt


# iterative
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        def recursive(rx, cy):
            if rx < 0 or rx >= rows or cy < 0 or cy >= cols or grid[rx][cy] != "1":
                return

            grid[rx][cy] = "0"

            for i in range(4):
                recursive(rx+dx[i], cy+dy[i])
            return

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] != "1":
                    continue

                cnt += 1
                recursive(row, col)

        return cnt


if __name__ == "__main__":
    solution = Solution2()
    print(solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1)

    print(solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3)

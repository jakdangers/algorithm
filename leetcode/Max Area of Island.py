class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        mx_r = len(grid)
        mx_c = len(grid[0])
        res = 0

        for r0 in range(mx_r):
            for c0 in range(mx_c):
                if grid[r0][c0] == 0:
                    continue
                stack = [(r0, c0)]
                area = 0
                while stack:
                    r, c = stack.pop()
                    print(grid[r][c])
                    if grid[r][c] == 1:
                        area += 1

                    grid[r][c] = 0

                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc]):
                            stack.append((nr, nc))
                print("===========")
                res = max(res, area)

        return res
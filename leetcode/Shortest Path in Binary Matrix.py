from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        mx = len(grid)

        def availableMoves(r, c):
            res = []

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if new_r >= 0 and new_r < mx and new_c >= 0 and new_c < mx and grid[new_r][new_c] == 0:
                    res.append((new_r, new_c))

            return res

        if grid[0][0] == 1 or grid[mx - 1][mx - 1] == 1:
            return -1

        queue = deque()
        queue.append((0, 0, 1))
        grid[0][0] = 1

        while queue:
            r, c, distance = queue.popleft()

            if r == mx - 1 and c == mx - 1:
                return distance

            visitable = availableMoves(r, c)

            for vr, vc in visitable:
                grid[vr][vc] = 1
                queue.append((vr, vc, distance + 1))

        return -1


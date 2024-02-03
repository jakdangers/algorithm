from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        start = (entrance[0], entrance[1], 0)
        queue = deque()
        queue.append(start)

        max_r = len(maze) - 1
        max_c = len(maze[0]) - 1

        def availableMoves(r, c):
            res = []
            for mr, mc in directions:
                new_r = r + mr
                new_c = c + mc

                if new_r >= 0 and new_r <= max_r and new_c >= 0 and new_c <= max_c and maze[new_r][new_c] == ".":
                    res.append((new_r, new_c))
            return res

        while queue:
            r, c, distance = queue.popleft()

            if (r, c) != (entrance[0], entrance[1]) and (max_r == r or r == 0 or c == 0 or max_c == c):
                return distance

            visitable = availableMoves(r, c)

            for nr, nc in visitable:
                maze[nr][nc] = "+"
                queue.append((nr, nc, distance + 1))

        return -1
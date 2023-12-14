class Solution:
    def isPathCrossing(self, path: str) -> bool:

        logs = set()

        start = (0, 0)
        logs.add(start)

        for p in path:

            if p == "N":
                start = (start[0], start[1] + 1)

            if p == "E":
                start = (start[0] + 1, start[1])

            if p == "S":
                start = (start[0], start[1] - 1)

            if p == "W":
                start = (start[0] - 1, start[1])

            if start in logs:
                return True

            logs.add(start)

        return False
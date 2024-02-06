from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        queue = deque()
        queue.append(start)

        seen = [False] * len(arr)
        seen[start] = True

        n = len(arr)

        # 범위를 벗어나면 큐에 담지 않는다

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True

            if idx + arr[idx] < n and not seen[idx + arr[idx]]:
                seen[idx + arr[idx]] = True
                queue.append(idx + arr[idx])

            if idx - arr[idx] >= 0 and not seen[idx - arr[idx]]:
                seen[idx - arr[idx]] = True
                queue.append(idx - arr[idx])

        return False





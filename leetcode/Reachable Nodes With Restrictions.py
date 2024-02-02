from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        result = 0

        seen = [False] * n
        for node in restricted:
            seen[node] = True

        def dfs(node):
            nonlocal result
            if seen[node]:
                return 0

            seen[node] = True
            result += 1

            for next_node in graph[node]:
                if not seen[next_node]:
                    dfs(next_node)

        dfs(0)

        return result



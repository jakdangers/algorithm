class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        path = []
        paths = []

        def dfs(node):
            path.append(node)

            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            visitable = graph[node]
            for next_node in visitable:
                dfs(next_node)
                path.pop()

        dfs(0)

        return paths






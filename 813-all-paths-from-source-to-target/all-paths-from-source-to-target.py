class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        TARGET = len(graph) - 1
        SOURCE = 0
        result = []
        
        def dfs(node, path):
            nonlocal result
            if node == TARGET:
                result.append(path.copy())
                return 

            for nb in graph[node]:
                path.append(nb)
                dfs(nb, path)
                path.pop()

        dfs(SOURCE, [SOURCE])

        return result
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        SOURCE = 0
        TARGET = len(graph) - 1
        paths = []
        def dfs(node, path):
            nonlocal paths
            if node == TARGET:
                paths.append(path)
            
            for nb in graph[node]:
                dfs(nb, path + [nb])
        
        dfs(0, [0])

        return paths
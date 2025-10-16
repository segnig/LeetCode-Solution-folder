class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        TARGET = len(graph) - 1
        SOURCE = 0
        result = []
        
        def helper(node, path):
            nonlocal result
            if node == TARGET:
                result.append(path[::])
            
            for nb in graph[node]:
                path.append(nb)
                helper(nb, path)
                path.pop()  
        
        helper(SOURCE, [SOURCE])
        
        return result
        
        
        
        """
        Target = n - 1 
        source = 0
        
        """
        
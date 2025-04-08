class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = defaultdict(list)

        # Track the neighbour node has the same color or not
        self.colors = [-1] * n

        # graph construction
        for s, d in dislikes:
            self.graph[s].append(d)
            self.graph[d].append(s)
        
        # Check for every nodes
        result = True
        for node in range(1, n + 1):
            # if not colored yet apply dfs 
            if self.colors[node-1] == -1:
                self.colors[node-1] = 1
                result = result and self.dfs(node)
        
        return result


    # DFS 
    def dfs(self, node):

        temp = True
        for neighbour in self.graph[node]:
            # if neighbour not colored yet
            if self.colors[neighbour - 1] == -1:
                
                # colored with opposite color
                if self.colors[node - 1] == 0:
                    self.colors[neighbour - 1] == 1
                else:
                    self.colors[neighbour - 1] = 0

                # recurtion call over neighbour node
                temp = temp and self.dfs(neighbour)

            # if colored and has the same color with its para
            elif self.colors[neighbour - 1] == self.colors[node - 1]:
                return False
            
        return temp

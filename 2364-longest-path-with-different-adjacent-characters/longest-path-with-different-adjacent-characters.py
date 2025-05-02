class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.graph = defaultdict(list)
        self.result = 1
        self.s = s
        
        for node, par in enumerate(parent):
            if node != 0:
                self.graph[par].append(node)
        self.queue = deque([0])
        while self.queue:
            node = self.queue.popleft()
            self.dfs(node)
        return self.result

    def dfs(self, node):
        if not self.graph[node]:
            return 1
        
        next_max = 0
        max_ = 0
        for child in self.graph[node]:
            if self.s[node] != self.s[child]:
                depth = self.dfs(child)

                if depth >= max_ :
                    next_max = max_
                    max_ = depth
                elif depth > next_max:
                    next_max = depth
            else:
                self.queue.append(child)
        self.result = max(self.result, max_ + next_max + 1)

        return max_ + 1
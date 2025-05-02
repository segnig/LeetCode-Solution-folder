class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # start_row, end_row, start_col, end_col
        range_dict = {}

        graph = defaultdict(set)

        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[0])):
                if targetGrid[i][j] not in range_dict:
                    range_dict[targetGrid[i][j]]  = [i, i, j, j]
                range_dict[targetGrid[i][j]][0] = min(range_dict[targetGrid[i][j]][0], i)
                range_dict[targetGrid[i][j]][1] = max(range_dict[targetGrid[i][j]][1], i)
                range_dict[targetGrid[i][j]][2] = min(range_dict[targetGrid[i][j]][2], j)
                range_dict[targetGrid[i][j]][3] = max(range_dict[targetGrid[i][j]][3], j)

        indegree = defaultdict(int)
        for color in range_dict:
            sr, er, sc, ec = range_dict[color]
            for i in range(sr, er+1):
                for j in range(sc, ec+1):
                    if color != targetGrid[i][j]:
                        if color not in graph[targetGrid[i][j]]:
                            graph[targetGrid[i][j]].add(color)
                            indegree[color] += 1

        
        queue = deque()

        for node in range_dict:
            if indegree[node] == 0:
                queue.append(node)

        count = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                count += 1
                for nb in graph[node]:
                    indegree[nb] -= 1
                    if indegree[nb] == 0:
                        queue.append(nb)

        return count == len(range_dict)
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        unique_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = unique_group
                unique_group += 1
        
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * unique_group
        
        for i in range(n):
            for j in beforeItems[i]:
                item_graph[j].append(i)
                item_indegree[i] += 1
                if group[i] != group[j]:
                    group_graph[group[j]].append(group[i])
        
        for g in group_graph:
            group_graph[g] = list(set(group_graph[g]))
            for dep_g in group_graph[g]:
                group_indegree[dep_g] += 1
        
        group_order = self.topo_sort(group_graph, group_indegree, unique_group)
        if not group_order:
            return []
        
        group_to_items = defaultdict(list)
        for i in range(n):
            group_to_items[group[i]].append(i)
        
        item_order = []
        for g in group_order:
            items_in_group = group_to_items[g]
         
            subgraph = defaultdict(list)
            sub_indegree = defaultdict(int)
            for i in items_in_group:
                for j in item_graph[i]:
                    if group[j] == g:  
                        subgraph[i].append(j)
                        sub_indegree[j] += 1
            
            queue = deque([i for i in items_in_group if sub_indegree[i] == 0])
            sorted_items = []
            while queue:
                i = queue.popleft()
                sorted_items.append(i)
                for j in subgraph[i]:
                    sub_indegree[j] -= 1
                    if sub_indegree[j] == 0:
                        queue.append(j)
            
            if len(sorted_items) != len(items_in_group):
                return []
            
            item_order.extend(sorted_items)
        
        return item_order
    
    def topo_sort(self, graph, indegree, size):
        queue = deque([node for node in range(size) if indegree[node] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == size else []
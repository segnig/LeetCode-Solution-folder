class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])

        while queue:
            key = queue.popleft()
            for nb in rooms[key]:
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
        return len(visited) == len(rooms)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        que = deque(["0000"])
        visited = set(["0000"])
        count = 0

        while que:
            count += 1
            temp = que
            que = deque()
            while temp:
                node = temp.popleft()
                for i in range(4):
                    left=node[:i]+str((int(node[i]) + 9) % 10) + node[i+1:]
                    right=node[:i]+str((int(node[i]) - 9) % 10) + node[i+1:]
                    if right not in deadends and right not in visited:
                        que.append(right)
                        visited.add(right)
                    if left not in deadends and left not in visited:
                        que.append(left)
                        visited.add(left)
                    if left == target or right == target:
                        return count
         
        return -1
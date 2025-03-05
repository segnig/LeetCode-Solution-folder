class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0

        for dir in logs:
            if dir == "../":
                if stack:
                    stack -= 1
            elif dir != "./":
                stack += 1

        return stack
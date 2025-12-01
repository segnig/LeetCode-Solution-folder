class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right =  1, sum(batteries) // n

        while left <= right:
            target = left + (right - left) // 2

            possible = 0

            for battery in batteries:
                possible += min(battery, target)

            if possible // n >= target:
                left = target + 1
            else:
                right = target - 1
        
        return right
        
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        ml = height[0]
        mr = height[-1]
        left = 0
        right = len(height) - 1

        result = 0
        while left < right:
            if ml < mr:
                left += 1
                ml = max(height[left], ml)
                result += ml - height[left]
            else:
                right -= 1
                mr = max(height[right], mr)
                result += mr - height[right]
        return result
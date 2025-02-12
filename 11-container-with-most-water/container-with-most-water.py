class Solution:
    def maxArea(self, height: List[int]) -> int:

        result = 0

        left = 0
        right = len(height) - 1

        while right  > left:
            result = max(result, min(height[left], height[right]) * (right - left))

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return result
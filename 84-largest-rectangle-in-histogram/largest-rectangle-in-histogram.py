class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        Area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height  = stack.pop()
                Area = max(Area, height * (i - index))
                start = index
            stack.append((start, h))
        
        end = len(heights)

        for i, h in stack:
            Area = max(Area, h * (end - i))
        
        return Area

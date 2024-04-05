class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
                print(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    r = stack.pop()
                    result[r] = i - r   
                stack.append(i)
        return result
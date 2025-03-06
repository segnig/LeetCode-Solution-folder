class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prev_smaller = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            else:
                prev_smaller[i] = -1
            stack.append(i)
        
        next_smaller = [n] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            else:
                next_smaller[i] = n
            stack.append(i)
        
        total = 0
        for i in range(n):
            count = (i - prev_smaller[i]) * (next_smaller[i] - i)
            total += arr[i] * count
            total %= MOD
        
        return total % MOD
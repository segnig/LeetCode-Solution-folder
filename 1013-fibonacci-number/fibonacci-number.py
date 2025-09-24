class Solution:
    def fib(self, n: int) -> int:
        
        def fn(n):
            if n < 2:
                return n
            return fn(n-1) + fn(n-2)
        
        return fn(n)


        
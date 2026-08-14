class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            num = 1
            for d in str(n):
                num *= int(d)

            if num % t == 0:
                return n

            n += 1
        
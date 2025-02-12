class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = int(math.sqrt(c))

        a = 0

        while d >= a:
            if d ** 2 + a ** 2 == c: 
                return True
            elif d ** 2 + a ** 2 > c:
                d -= 1
            else:
                a += 1

        return False
        
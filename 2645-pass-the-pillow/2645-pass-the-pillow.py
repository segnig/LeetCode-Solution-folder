class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        upWard = True
        res = 0
        while time:
            if res == 0:
                upWard = True
            if res == n - 1:
                upWard = False
            if upWard:
                res += 1
            else:
                res -= 1
            time -= 1
        return res + 1

        

"""
1  2  3  4  5
  - -   -  -

"""